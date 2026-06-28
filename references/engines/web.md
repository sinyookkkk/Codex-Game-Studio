# Web Game Reference

Use for browser-based games.

## Architecture

- Keep rendering loop, input, game state, and UI overlays separate.
- Test keyboard, pointer, touch, focus, and audio unlock behavior.
- Use stable canvas sizing and device pixel ratio handling.
- Keep asset loading visible and recoverable.

## Checks

- Build and dev commands are documented.
- Game works at target aspect ratios.
- Audio starts only after user gesture when required.
- Save storage behavior is tested.
- Mobile and desktop input assumptions are explicit.

## Common risks

- Canvas or UI text overflow on mobile.
- Browser autoplay/audio restrictions.
- Input focus lost after pause or fullscreen changes.
