# 👍 Facebook Auto-Liker
**Simple, Hacky, and Efficient Bot for Social Automation**

[![Tested on Gemini](https://img.shields.io/badge/Tested_on-Gemini_CLI-8E44AD?style=for-the-badge&logo=google-gemini&logoColor=white)](https://github.com/google/gemini-cli)
[![Tech Stack: Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Library: PyAutoGUI](https://img.shields.io/badge/Library-PyAutoGUI-blue?style=for-the-badge)](https://pyautogui.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Facebook Auto-Liker** is a lightweight Python script that uses computer vision and keyboard/mouse automation via `PyAutoGUI` to automatically like images on Facebook. It's a "set and forget" tool for social interaction.

`✅ Social Automation | ✅ Computer Vision | ✅ MIT Licensed | ✅ 45+ Stars Utility`

## 🎬 Showcase Gallery
| 🖼️ Pattern Matching | 📟 Automation Logic |
| :---: | :---: |
| ![Detection](https://raw.githubusercontent.com/ayushxx7/Facebook-Auto-Liker/master/newlikeButton.PNG) | ![Flow](https://raw.githubusercontent.com/ayushxx7/Facebook-Auto-Liker/master/likeButtonOnFB.PNG) |

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
- **Automation Logic (`autoLikeFB.py`)**: The main driver script that handles timing, coordinate calculation, and loop control.
- **Pattern Matching (`likeButtonOnFB.PNG`)**: The reference image used by PyAutoGUI to locate the target element on the screen.
- **Environment Logic**: Uses `time.sleep()` for surgical pacing between interactions to avoid detection.

## 🚀 Getting Started

1. **Install Dependencies**:
   ```bash
   pip install pyautogui
   ```

2. **Configuration**:
   Ensure you have a screenshot of the Facebook Like button named `likeButtonOnFB.PNG` in the project root (tailored to your monitor resolution).

3. **Execution**:
   Run the script and immediately switch to your Facebook tab (Alt+Tab).

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---
*Built with ❤️ for Social Automation.*
