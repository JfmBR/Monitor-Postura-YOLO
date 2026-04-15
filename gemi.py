import cv2
from ultralytics import YOLO

# 1. Carregar o modelo de pose
model = YOLO('yolov8n-pose.pt')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    results = model(frame, verbose=False)

    for r in results:
        annotated_frame = r.plot()
        
        # Verificamos se há pontos suficientes (precisamos de nariz e ombros)
        if r.keypoints is not None and len(r.keypoints.xy[0]) > 6:
            points = r.keypoints.xy[0].cpu().numpy()
            
            # Mapeamento de pontos
            # Nariz = 0, Ombro Esq = 5, Ombro Dir = 6
            nariz = points[0]
            ombro_esq = points[5]
            ombro_dir = points[6]

            # --- LÓGICA PARA DETECTAR "CORCUNDA" ---
            # 1. Calculamos a altura média dos ombros (Y)
            altura_media_ombros = (ombro_esq[1] + ombro_dir[1]) / 2
            
            # 2. Calculamos a distância vertical entre o nariz e os ombros
            # Se a pessoa se curva, essa distância diminui
            distancia_pescoço = altura_media_ombros - nariz[1]
            
            # Configuração de alertas
            postura_status = "Boa Postura"
            cor_alerta = (0, 255, 0) # Verde

            # Se a distância for muito pequena, a pessoa está curvada (corcunda)
            # DICA: 70 é um valor base, você pode precisar ajustar conforme a distância da câmera
            if distancia_pescoço < 70:
                postura_status = "ALERTA: Nao fique corcunda!"
                cor_alerta = (0, 0, 255) # Vermelho
            
            # Verificação extra: Ombros desalinhados (lateral)
            elif abs(ombro_esq[1] - ombro_dir[1]) > 30:
                postura_status = "Ma Postura: Ombros Desalinhados"
                cor_alerta = (0, 0, 255)

            # 4. Interface Visual
            cv2.rectangle(annotated_frame, (10, 10), (500, 60), (255, 255, 255), -1)
            cv2.putText(annotated_frame, f"{postura_status} ({int(distancia_pescoço)})", 
                        (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, cor_alerta, 2)

    cv2.imshow("Monitor de Saude - Ergonomia", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()