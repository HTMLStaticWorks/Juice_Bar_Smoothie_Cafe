---
name: Vibrant Health & Juice
colors:
  surface: '#ecffe5'
  surface-dim: '#cce0c6'
  surface-bright: '#ecffe5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e5f9df'
  surface-container: '#dff4d9'
  surface-container-high: '#daeed4'
  surface-container-highest: '#d4e8ce'
  on-surface: '#0f1f0f'
  on-surface-variant: '#41493e'
  inverse-surface: '#243423'
  inverse-on-surface: '#e2f7dc'
  outline: '#717a6d'
  outline-variant: '#c0c9bb'
  surface-tint: '#2a6b2c'
  primary: '#00450d'
  on-primary: '#ffffff'
  primary-container: '#1b5e20'
  on-primary-container: '#90d689'
  inverse-primary: '#91d78a'
  secondary: '#705d00'
  on-secondary: '#ffffff'
  secondary-container: '#fdd400'
  on-secondary-container: '#6f5c00'
  tertiary: '#770044'
  on-tertiary: '#ffffff'
  tertiary-container: '#a1005d'
  on-tertiary-container: '#ffaecb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#acf4a4'
  primary-fixed-dim: '#91d78a'
  on-primary-fixed: '#002203'
  on-primary-fixed-variant: '#0c5216'
  secondary-fixed: '#ffe170'
  secondary-fixed-dim: '#e9c400'
  on-secondary-fixed: '#221b00'
  on-secondary-fixed-variant: '#544600'
  tertiary-fixed: '#ffd9e4'
  tertiary-fixed-dim: '#ffb0cc'
  on-tertiary-fixed: '#3e0021'
  on-tertiary-fixed-variant: '#8d0051'
  background: '#ecffe5'
  on-background: '#0f1f0f'
  surface-variant: '#d4e8ce'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  section-gap: 80px
---

## Brand & Style
The design system embodies a "Premium Organic" aesthetic, blending the freshness of natural ingredients with the precision of a modern SaaS interface. The target audience is health-conscious, active individuals who value both wellness and high-end digital experiences. 

The style is **Corporate Modern with a Tactile twist**. It utilizes heavy whitespace to evoke a sense of cleanliness and purity, while vibrant accents create an energetic, "freshly squeezed" emotional response. Transitions should be fluid and organic, avoiding rigid or mechanical easing.

## Colors
The palette is rooted in a "Deep Tropical Green" to establish authority and health. The "Citrus Zest Yellow" provides high-energy highlights, while "Berry Burst Magenta" is used sparingly for critical call-to-actions or flavor-specific highlights.

In **Light Mode**, the background uses a subtle minty-white to reduce eye strain compared to pure white. In **Dark Mode**, the surfaces shift to deep forest tones to maintain the organic narrative while providing high contrast for the neon-leaning accent colors.

## Typography
Plus Jakarta Sans (selected as the closest high-quality match to Poppins' geometric clarity) is used for all headings to provide a premium, modern feel. All headlines must be **center-aligned** across all screen sizes to maintain a focused, editorial layout.

Inter is utilized for body text and labels to ensure maximum legibility and a systematic, SaaS-like precision. Use higher line-heights for body text to maintain the "airy" and "fresh" brand promise.

## Layout & Spacing
The layout follows a **fluid grid** model based on an 8px base unit. To achieve the "Modern SaaS" feel, use generous vertical padding between sections (80px+). 

Content is centered globally. Cards and containers should use symmetrical internal padding. Desktop layouts utilize a 12-column grid, while mobile scales down to a single-column stack with all elements—including icons and text—retaining their center alignment.

## Elevation & Depth
The design system uses **Tonal Layers** combined with **Ambient Shadows**. Surfaces do not use harsh borders; instead, they are defined by soft, diffused shadows with a slight green tint (`rgba(27, 94, 32, 0.08)`) in light mode.

In dark mode, depth is achieved through slight shifts in luminosity (surface-container logic) rather than shadows. Interactive elements like cards should employ a "lift" effect on hover, increasing shadow spread and slightly scaling up (1.02x) to mimic physical responsiveness.

## Shapes
The shape language is consistently **Rounded** (Level 2). This reflects the organic nature of fruits and liquids. All buttons, input fields, and cards must share the exact same corner radius (0.5rem / 8px) to maintain visual harmony. Large feature cards may use `rounded-xl` (1.5rem) for a softer, more "premium" feel.

## Components
- **Buttons:** Primary buttons are solid "Deep Tropical Green" with white text. Secondary buttons use a thick 2px border of the same green. All buttons feature center-aligned text and high-contrast labels.
- **Cards:** White or dark-forest background with center-aligned headers and icons. All card content (text, icons, prices) must be horizontally centered.
- **Inputs:** Clean, outlined fields with a 2px stroke. On focus, the stroke changes to "Citrus Zest Yellow" to provide a vibrant feedback loop.
- **Chips/Badges:** Small, high-contrast pills using the Berry Burst Magenta for nutritional callouts (e.g., "High Protein", "Vegan").
- **Lists:** Icon-led lists where the icon is placed directly above the text label (center-aligned), rather than to the left, to maintain the vertical symmetry of the system.