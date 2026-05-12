# Remotion API Reference

## Core Hooks

### `useCurrentFrame()`
Returns the current frame number (0-indexed integer). The primary driver of all animation.

### `useVideoConfig()`
Returns `{ fps, durationInFrames, width, height, id, defaultProps }` for the current composition.

### `useDelayRender()`
Returns `{ delayRender, continueRender }`. Call `delayRender(label?)` to pause rendering, `continueRender(handle)` when async work is done. Must resolve within 30s.

### `useBufferState()`
Returns `{ isBuffering }`. Useful to pause playback in `<Player>` while media loads.

### `useCurrentScale()`
Returns the current scale of the composition (useful in `<Player>` embedded at non-native sizes).

## Core Components

### `<AbsoluteFill>`
Full-canvas `position: absolute` container filling 100% width/height. Supports `style` and `className` passthrough.

### `<Composition>`
Registers a video for rendering. Required props: `id`, `component`, `durationInFrames`, `fps`, `width`, `height`. Optional: `defaultProps`, `schema` (Zod), `calculateMetadata`, `lazyComponent`.

### `<Sequence>`
Props: `from` (frame offset, default 0), `durationInFrames` (default Infinity), `layout` (`'absolute-fill'` | `'none'`), `name`, `style`, `className`, `premountFor`, `postmountFor`.

### `<Series>` / `<Series.Sequence>`
Automatic sequential layout. `<Series.Sequence>` requires `durationInFrames`. Optional `offset` prop to add a gap between clips.

### `<Loop>`
Props: `durationInFrames` (loop period), `times` (repetitions, default Infinity), `layout`.

### `<Still>`
Registers a single-frame composition. Props: `id`, `component`, `width`, `height`. No `fps` or `durationInFrames`.

### `<Folder>`
Groups compositions in Remotion Studio sidebar. Props: `name`.

### `<Video>` / `<OffthreadVideo>`
Embed video file. Props: `src`, `startFrom`, `endAt`, `volume`, `muted`, `loop`, `playbackRate`, `style`. Prefer `OffthreadVideo` for rendering accuracy.

### `<Audio>`
Embed audio. Props: `src`, `volume` (0–1 or frame→number function), `startFrom`, `endAt`, `muted`, `loop`, `playbackRate`.

### `<Img>`
Like `<img>` but delays rendering until fully loaded. Props: same as HTML `<img>`.

### `<IFrame>`
Embeds an iframe, delays rendering until load event fires.

## Utility Functions

### `interpolate(value, inputRange, outputRange, options?)`
- `options.extrapolateLeft` / `options.extrapolateRight`: `'clamp'` | `'extend'` | `'wrap'` | `'identity'`
- `options.easing`: easing function (see `Easing` from `remotion`)

### `interpolateColors(value, inputRange, outputRange, options?)`
Same API as `interpolate` but output values are CSS color strings. Supports hex, rgb, hsl.

### `spring({ frame, fps, config?, from?, to?, durationInFrames?, delay?, reverse?, overshootClamping? })`
- `config.mass` (default 1), `config.damping` (default 10), `config.stiffness` (default 100)
- `overshootClamping: true` disables bounce past target

### `staticFile(path)`
Returns the URL of a file in the `public/` directory. Works in both development and rendering.

### `random(seed)`
Deterministic pseudo-random number (0–1) based on seed. Same seed always returns same value across frames — use for stable noise, e.g., `random('particle-x-' + i)`.

### `getInputProps()`
Retrieves input props passed via `--props` flag during render or programmatic API.

### `getStaticFiles()`
Returns an array of all files in `public/`, useful for dynamic file lists.

### `prefetch(src, options?)`
Pre-fetches a remote media file. Returns `{ waitUntilDone, free }`.

### `delayRender(label?, options?)` / `continueRender(handle)` / `cancelRender(err)`
Lower-level versions of `useDelayRender`. Use inside components only.

## Easing

Import `Easing` from `remotion`:

```tsx
import { Easing, interpolate } from 'remotion';

const val = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0.25, 0.1, 0.25, 1),
  extrapolateRight: 'clamp',
});
```

Built-ins: `Easing.linear`, `Easing.ease`, `Easing.quad`, `Easing.cubic`, `Easing.sin`, `Easing.circle`, `Easing.exp`, `Easing.elastic(bounciness)`, `Easing.bounce`, `Easing.back(s)`, `Easing.bezier(x1,y1,x2,y2)`, `Easing.in(e)`, `Easing.out(e)`, `Easing.inOut(e)`.

## `calculateMetadata`

Dynamically compute composition metadata from props (including async data):

```tsx
<Composition
  id="Dynamic"
  component={MyComp}
  calculateMetadata={async ({ props }) => {
    const data = await fetchData(props.id);
    return {
      durationInFrames: data.frames,
      props: { ...props, data },
    };
  }}
  defaultProps={{ id: 'abc' }}
  fps={30} width={1920} height={1080}
/>
```

## `@remotion/player`

Embed a Remotion composition in a React web app:

```bash
npm install @remotion/player
```

```tsx
import { Player } from '@remotion/player';
import { MyVideo } from './MyVideo';

<Player
  component={MyVideo}
  durationInFrames={150}
  fps={30}
  compositionWidth={1920}
  compositionHeight={1080}
  style={{ width: 640 }}
  controls
  loop
/>
```

## Cloud Rendering

### Lambda (`@remotion/lambda`)
Render on AWS Lambda. Setup: `npx remotion lambda functions deploy`. Programmatic API: `renderMediaOnLambda()`.

### Google Cloud Run (`@remotion/cloudrun`)
Alternative to Lambda for GCP environments.

### GitHub Actions
Use `@remotion/renderer` directly in CI with `renderMedia()` from the Node.js API.

## Node.js / Server-Side API (`@remotion/renderer`)

```bash
npm install @remotion/renderer
```

```ts
import { renderMedia, selectComposition } from '@remotion/renderer';

const composition = await selectComposition({
  serveUrl: bundleUrl,
  id: 'MyVideo',
});

await renderMedia({
  composition,
  serveUrl: bundleUrl,
  codec: 'h264',
  outputLocation: 'out.mp4',
});
```

## CLI Config (`remotion.config.ts`)

```ts
import { Config } from '@remotion/cli/config';

Config.setConcurrency(4);
Config.setCodec('h264');
Config.setQuality(90);
Config.setOutputLocation('out/video.mp4');
```

## Common Packages

| Package | Purpose |
|---|---|
| `@remotion/player` | Embed video player in React apps |
| `@remotion/renderer` | Server-side / Node.js rendering |
| `@remotion/lambda` | AWS Lambda cloud rendering |
| `@remotion/cloudrun` | Google Cloud Run rendering |
| `@remotion/gif` | Render GIFs frame-accurately |
| `@remotion/media-utils` | `getVideoMetadata`, `getAudioData`, `visualizeAudio` |
| `@remotion/google-fonts` | Load Google Fonts reliably |
| `@remotion/fonts` | Load local fonts |
| `@remotion/three` | React Three Fiber integration |
| `@remotion/lottie` | Render Lottie animations |
| `@remotion/motion-blur` | Camera-style motion blur |
| `@remotion/noise` | Deterministic Perlin/Simplex noise |
| `@remotion/paths` | SVG path animation utilities |
| `@remotion/shapes` | Animated SVG shape generators |
| `@remotion/rive` | Rive animation integration |
| `@remotion/skia` | React Native Skia integration |
