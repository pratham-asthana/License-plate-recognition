# License Plate Recognition 🚗🔍

This project implements a **License Plate Recognition System** using **OpenCV**, **EasyOCR**, and **Python**. The system detects and extracts license plates from vehicle images and applies Optical Character Recognition (OCR) to retrieve the plate numbers.

## 📸 Demo

![Demo Image](https://github.com/pratham-asthana/License-plate-recognition/blob/main/Images/Output.jpg)

## 🧠 Features

* 🚘 License plate detection using OpenCV and contour methods.
* 🧾 Text extraction using EasyOCR (supports multiple languages).
* 🖼️ Visual output with bounding boxes and annotated plate numbers.
* 📁 Simple and modular codebase—easy to extend to video input or real-time feed.

---

## 🗂️ Project Structure

```
License-plate-recognition/
├── main.py              # Main script to run recognition
├── detect.py            # License plate detection logic
├── read_plate.py        # OCR and plate text reading
├── Images/              # Input and output images
│   ├── car1.jpg
│   └── Output.jpg
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```

---

## ⚙️ Installation

Make sure you have **Python 3.7+** installed. Then follow these steps:

```bash
# Clone the repository
git clone https://github.com/pratham-asthana/License-plate-recognition.git
cd License-plate-recognition

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Place an input image

Put your vehicle image inside the `Images/` folder.

### 2. Run the main script

```bash
python main.py
```

The output image with detected license plate and recognized number will be saved in the `Images/` folder.

---

## 🧾 Example

Input:

![Input Image](https://github.com/pratham-asthana/License-plate-recognition/blob/main/Images/car1.jpg)

Output:

![Output Image](https://github.com/pratham-asthana/License-plate-recognition/blob/main/Images/Output.jpg)

---

## 📦 Requirements

* `opencv-python`
* `easyocr`
* `numpy`

Install with:

```bash
pip install opencv-python easyocr numpy
```

---

## 🧹 Future Improvements

* Real-time license plate recognition via webcam/video
* Region-specific plate formatting (e.g., Indian plates, EU plates)
* Accuracy improvements with deep learning models (YOLO, Faster R-CNN)
* GUI interface using Streamlit or Tkinter

---

## 🧑‍💻 Author

**Pratham Asthana**
📧 [prathamasthana04@gmail.com](mailto:prathamasthana04@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/pratham-asthana-243133265) • [GitHub](https://github.com/pratham-asthana)

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute it for personal or commercial purposes.

---

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
