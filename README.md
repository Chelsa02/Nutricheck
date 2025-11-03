
# Nutricheck (Expo + React Native)

Production-ready scaffold for the Nutricheck mobile app. Includes a clean folder structure, working navigation, and mock data.

## Project structure

```
Nutricheck/
├─ App.js                 # Navigation container and stack
├─ app.json               # Expo app config
├─ package.json           # Dependencies and scripts
├─ screens/
│  ├─ HomeScreen.js
│  ├─ MealPlanScreen.js
│  ├─ RecommendationScreen.js
│  └─ SettingsScreen.js
├─ components/
│  └─ MealCard.js
├─ data/
│  └─ sampleMeals.json
└─ .gitignore
```

## Run locally
1. Install Node.js (LTS) and npm.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the app (Expo Metro bundler):
   ```bash
   npm start
   ```
4. Open on device (Expo Go) or on Android/iOS emulator from the Metro UI.

## Build for release (EAS Build)

EAS Build is the recommended way to create production binaries (APK/AAB/IPA).

Prereqs:
- Expo account (run `npx expo login`)
- Android: no Apple requirements; iOS: requires Apple developer account for publishing.

Commands:
```bash
# Configure EAS if first time
npx expo install eas-cli
npx eas login

# Android build (AAB by default)
npx eas build --platform android

# iOS build
npx eas build --platform ios
```

The build artifacts will be available on the EAS website with a shareable URL. You can submit directly with:
```bash
npx eas submit --platform android
npx eas submit --platform ios
```

## Notes
- App icons and splash are currently using Expo defaults. To customize, add images to `assets/` and set `icon` and `splash` in `app.json`.
- Unused deps were removed for a slimmer build. Add only what you use.

## Deploy to Vercel (Web)

This project can be exported as a static web app and hosted on Vercel.

Already configured:
- Script: `npm run build:web` (exports to `dist/`)
- `vercel.json` with build command, output directory, and SPA rewrites

Steps:
1. Build the static site:
   ```bash
   npm run build:web
   ```
2. Connect the repo to Vercel and set:
   - Build Command: `npm run build:web`
   - Output Directory: `dist`
3. Deploy. Vercel will serve `dist/` with client-side routing supported.

Notes:
- If you add custom routes or slug-based screens, the SPA rewrite in `vercel.json` ensures index.html is returned.
- For environment variables, add them in Vercel Project Settings; Expo will inline them at build time if referenced.
