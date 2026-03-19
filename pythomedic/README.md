# Pythomedic

AI-powered plant disease detection and robotic pesticide sprayer — Android app.

Based on published research achieving **99.4% accuracy** on a 3,243-image dataset using OpenCV & NumPy.

## Team

| Name | Area |
|---|---|
| Emmanuel Oppong | ML + Backend (diagnose API) |
| Emmanuel Acheampong | Android App |
| Micheal Akontoke | Backend API + DevOps + IoT |

## Structure

```
pythomedic/
├── android/        ← Kotlin + Jetpack Compose Android app (Acheampong)
├── backend/        ← FastAPI Python backend (Oppong + Akontoke)
├── ml-research/    ← Training scripts + dataset (Oppong)
├── robot/          ← Raspberry Pi sprayer controller (Akontoke)
└── .github/        ← CI/CD workflows (Akontoke)
```

See `PYTHOMEDIC_BUILD.md` for full build plan and work division.
