# 👍 Facebook Auto-Liker
**Simple, Hacky, and Efficient Bot for Social Automation**

[![Tested on Gemini](https://img.shields.io/badge/Tested_on-Gemini_CLI-8E44AD?style=for-the-badge&logo=google-gemini&logoColor=white)](https://github.com/google/gemini-cli)
[![Tech Stack: Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

**Facebook Auto-Liker** is a lightweight Python script that uses computer vision and keyboard/mouse automation to automatically like images on Facebook. It's a "set and forget" tool for social interaction.

`✅ Social Automation | ✅ Computer Vision | ✅ MIT Licensed | ✅ 45+ Stars Utility`

## 🎬 Logic Preview
![Bot Preview](showcase/bot_preview.svg)

## 🏗 Architecture
The bot operates using a simple linear execution loop powered by Pixel Matching and GUI automation.

```mermaid
graph LR
    A[Start Script] --> B[Wait for Switch]
    B --> C{Detect Like Button?}
    C -- Yes --> D[Perform Click]
    D --> E[Next Image]
    E --> C
    C -- No --> F[Exit/Retry]
```

### Core Components
- **Automation Logic**: Driver script handling timing, coordinate calculation, and loop control.
- **Pattern Matching**: Reference images used by `PyAutoGUI` to locate target elements on screen.
- **Environment Pacing**: Surgical delays between interactions to maintain reliability.

## 🚀 Getting Started
```bash
pip install pyautogui
# Ensure likeButtonOnFB.PNG is in the root
python3 autoLikeFB.py
```

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---
*Built with ❤️ for Social Automation.*
