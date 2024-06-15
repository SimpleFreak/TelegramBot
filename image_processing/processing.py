import cv2
import os


class Processing:

    # Конструктор класса
    def __init__(self):
        model_path = os.path.dirname(os.path.realpath(
            ".\\models\\haarcascade_frontalface_default.xml"))
        path_model = f"{model_path}\\haarcascade_frontalface_default.xml"

        self.face_cascade = cv2.CascadeClassifier(path_model)

    # Метод для обработки изображений

    def save_swap_faces(self, source_image_file, replacement_image_file,
                        theme, result_image):

        # Загрузка изображений
        source_image = cv2.imread(source_image_file)
        replacement_image = cv2.imread(replacement_image_file)

        result = replacement_image.copy()

        # Преобразование изображений в оттенки серого
        gray_source_image = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
        gray_replacement_image = cv2.cvtColor(
            replacement_image, cv2.COLOR_BGR2GRAY)

        source_faces = self.face_cascade.detectMultiScale(gray_source_image,
                                                          scaleFactor=1.1,
                                                          minNeighbors=5,
                                                          flags=cv2.CASCADE_SCALE_IMAGE,
                                                          minSize=(30, 30))
        replacement_faces = self.face_cascade.detectMultiScale(gray_replacement_image,
                                                               scaleFactor=1.1,
                                                               minNeighbors=5,
                                                               flags=cv2.CASCADE_SCALE_IMAGE,
                                                               minSize=(30, 30))

        # Проверка на наличие лиц на обоих изображениях
        if len(source_faces) > 0 and len(replacement_faces) > 0:
            (x1, y1, w1, h1) = source_faces[0]
            (x2, y2, w2, h2) = replacement_faces[0]

            source_face = source_image[y1:y1+h1, x1:x1+w1]

            resized_face = cv2.resize(source_face, (w2, h2))

            result[y2:y2+h2, x2:x2+w2] = resized_face

            filename = f".\\media\\save_users_stickers\\{
                theme}\\{result_image}"

            # Сохранение результата в файле
            cv2.imwrite(filename, result)
            print(f"Результат сохранен в файле: {filename}")

        else:
            print("Не удалось обнаружить лица на обоих изображениях.")
