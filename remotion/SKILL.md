---
name: remotion
description: Create programmatic videos using React and Remotion. This skill should be used when users want to generate videos, animations, or motion graphics from code — including data visualizations, explainer videos, social media clips, dynamic text animations, and any video content driven by React components.
---

# Remotion Video Creation

Remotion is a framework for creating videos programmatically using React. Every frame is a React render; animations are driven by the current frame number.

## Project Setup

```bash
npx create-video@latest
cd my-video
npm run dev       # opens Remotion Studio at localhost:3000
```

Adding to an existing project:
```bash
npm install remotion @remotion/cli
```

Entry point is `src/Root.tsx` — register all compositions there.

## Core Mental Model

A Remotion video is a pure function of frame number → image. `useCurrentFrame()` returns the current frame (0-indexed). Change output based on this number to produce animation.

```tsx
import { useCurrentFrame, useVideoConfig, AbsoluteFill } from 'remotion';

export const MyVideo = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames, width, height } = useVideoConfig();

  const opacity = frame / 30; // fade in over 1 second at 30fps

  return (
    <AbsoluteFill style={{ backgroundColor: 'white' }}>
      <div style={{ opacity }}>Hello, world!</div>
    </AbsoluteFill>
  );
};
```

## Registering a Composition

In `src/Root.tsx`:
```tsx
import { Composition } from 'remotion';
import { MyVideo } from './MyVideo';

export const RemotionRoot = () => (
  <>
    <Composition
      id="MyVideo"
      component={MyVideo}
      durationInFrames={150}
      fps={30}
      width={1920}
      height={1080}
    />
  </>
);
```

Register `RemotionRoot` with `registerRoot` in the entry file (done automatically by the template).

## Animation Primitives

### interpolate()

Maps an input range to an output range. The most-used animation utility.

```tsx
import { interpolate } from 'remotion';

// Fade in frames 0–20, stay at 1 after
const opacity = interpolate(frame, [0, 20], [0, 1], {
  extrapolateRight: 'clamp',
});

// Scale up then back down
const scale = interpolate(frame, [0, 15, 30], [0.5, 1.2, 1], {
  extrapolateLeft: 'clamp',
  extrapolateRight: 'clamp',
});
```

`extrapolateLeft` / `extrapolateRight` options: `'clamp'` (most common), `'extend'`, `'wrap'`, `'identity'`.

### spring()

Physics-based animation with natural bounce/settle feel.

```tsx
import { spring } from 'remotion';

const scale = spring({
  frame,
  fps,
  config: { stiffness: 200, damping: 15 },
  from: 0,
  to: 1,
});
```

Config knobs: `stiffness` (speed), `damping` (reduces bounce), `mass`. Use `durationInFrames` to pin the animation to an exact length.

### interpolateColors()

```tsx
import { interpolateColors } from 'remotion';

const bg = interpolateColors(frame, [0, 60], ['#ffffff', '#1e293b']);
<AbsoluteFill style={{ backgroundColor: bg }} />
```

## Sequencing Content

### `<Sequence>`

Time-shifts children: child's `useCurrentFrame()` counts from 0 at the `from` frame.

```tsx
import { Sequence } from 'remotion';

<Sequence from={30} durationInFrames={60}>
  <Title />  {/* visible frames 30–89; its frame 0 = global frame 30 */}
</Sequence>
```

Nest sequences freely; offsets stack additively.

### `<Series>`

Lay out clips back-to-back without manual frame math.

```tsx
import { Series } from 'remotion';

<Series>
  <Series.Sequence durationInFrames={40}><Intro /></Series.Sequence>
  <Series.Sequence durationInFrames={80}><Main /></Series.Sequence>
  <Series.Sequence durationInFrames={30}><Outro /></Series.Sequence>
</Series>
```

### `<Loop>`

Repeat content N times (or infinitely).

```tsx
import { Loop } from 'remotion';

<Loop durationInFrames={30} times={5}>
  <BlinkingCursor />
</Loop>
```

## Media Components

```tsx
import { Video, Audio, Img, OffthreadVideo } from 'remotion';
import { staticFile } from 'remotion';

<OffthreadVideo src={staticFile('clip.mp4')} startFrom={30} endAt={90} />
<Audio src={staticFile('bg.mp3')} volume={0.6} />
<Img src={staticFile('logo.png')} />
```

Use `staticFile('filename')` for files in `public/`. Pass remote URLs directly as `src`.

Prefer `OffthreadVideo` over `Video` — it guarantees frame-accurate rendering during export.

## Async Data (delayRender)

To fetch data before rendering frames, use `useDelayRender`:

```tsx
import { useDelayRender, cancelRender } from 'remotion';
import { useState, useEffect } from 'react';

export const DataDrivenComp = () => {
  const { delayRender, continueRender } = useDelayRender();
  const [data, setData] = useState(null);
  const [handle] = useState(() => delayRender('Fetching data...'));

  useEffect(() => {
    fetch('/api/data')
      .then(r => r.json())
      .then(d => { setData(d); continueRender(handle); })
      .catch(err => cancelRender(err));
  }, []);

  if (!data) return null;
  return <div>{data.title}</div>;
};
```

`continueRender` must be called within 30 seconds or the render times out.

## Input Props

Pass external data into compositions:

```tsx
// Root.tsx
<Composition
  id="TitleCard"
  component={TitleCard}
  defaultProps={{ title: 'Hello', subtitle: 'World' }}
  durationInFrames={90} fps={30} width={1920} height={1080}
/>

// TitleCard.tsx
const TitleCard = ({ title, subtitle }: { title: string; subtitle: string }) => { ... };
```

Override at render time:
```bash
npx remotion render TitleCard out.mp4 --props='{"title":"Custom Title"}'
```

Add a Zod `schema` prop to `<Composition>` to enable visual prop editing in Remotion Studio.

## Rendering

```bash
# Interactive preview
npx remotion studio

# Render video
npx remotion render <CompositionId> output.mp4

# Render still frame
npx remotion still <CompositionId> frame.png --frame=30

# Render as GIF
npx remotion render <CompositionId> output.gif

# Render image sequence
npx remotion render <CompositionId> frames/ --sequence
```

Common render flags:
- `--codec=h264|h265|vp8|vp9|gif`
- `--crf=18` (quality; lower = better, default 18)
- `--frames=0-100` (partial render)
- `--concurrency=4` (parallel render threads)

## Common Patterns

### Staggered word fade-in

```tsx
const words = ['Build', 'videos', 'with', 'React'];

{words.map((word, i) => {
  const delay = i * 8;
  const opacity = interpolate(frame, [delay, delay + 15], [0, 1], {
    extrapolateRight: 'clamp',
  });
  return <span key={i} style={{ opacity, marginRight: 12 }}>{word}</span>;
})}
```

### Slide-up entrance with spring

```tsx
const slideY = spring({ frame, fps, from: 80, to: 0, config: { damping: 14 } });
const opacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: 'clamp' });

<div style={{ transform: `translateY(${slideY}px)`, opacity }}>
  Slides in from below
</div>
```

### Progress bar

```tsx
const progress = frame / durationInFrames;
<div style={{ width: `${progress * 100}%`, height: 8, background: '#3b82f6' }} />
```

### Looping typewriter cursor

```tsx
<Loop durationInFrames={30}>
  {(() => {
    const f = useCurrentFrame();
    return <span style={{ opacity: f < 15 ? 1 : 0 }}>|</span>;
  })()}
</Loop>
```

## Reference

See `references/api.md` for the complete API listing, less-common hooks, cloud rendering options, and `@remotion/player` embed docs.
