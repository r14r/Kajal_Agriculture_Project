# Navbar Quick Reference Card

## 🎨 Color Palette

```
Primary Green:    #2d6a4f
Light Green:      #40916c
Accent Green:     #52b788
Earthy Brown:     #8b6f47
Gold (NEW):       #ffd700
White:            #f1f5f4
Dark Text:        #1b3a2f
```

## 📐 Dimensions

```
LOGO:
Icon Size:        1.8rem
Icon Box:         50x50px
Icon Box Radius:  12px
Logo Main Font:   1.5rem
Logo Sub Font:    0.8rem

NAVIGATION:
Link Padding:     0.7rem 1.2rem
Link Font Size:   0.95rem
Underline Height: 2px
Underline Width:  80% (on hover)

LANGUAGE BUTTON:
Font Size:        0.9rem
Padding:          0.6rem 1rem
Border Radius:    8px
Icon Size:        1rem

HAMBURGER:
Width:            28px
Height:           3px each
Gap:              5px
Border Radius:    2px

NAVBAR HEIGHT:
Desktop:          70px
Scrolled:         65px
Mobile:           60px
```

## ⏱️ Animation Timing

```
ALL ANIMATIONS:
Duration:         0.3s
Easing:           ease
GPU Accelerated:  ✅ Yes
FPS Target:       60fps
```

## 🎬 Animation Sequences

```
LOGO HOVER:
- rotate(0deg) scale(1) 
  → rotate(10deg) scale(1.1)

LINK UNDERLINE HOVER:
- width: 0% 
  → width: 80%

LANGUAGE ICON HOVER:
- rotate(0deg) 
  → rotate(20deg)

HAMBURGER ACTIVE:
- Line 1: rotate(45deg) translate(10px,10px)
- Line 2: opacity(0)
- Line 3: rotate(-45deg) translate(8px,-8px)

SCROLL EFFECT (at 50px):
- Background: lighter → darker
- Shadow: 0 8px 24px → 0 12px 32px
- Padding: 0.8rem → 0.5rem
```

## 📱 Responsive Breakpoints

```
DESKTOP (1200px+):
├─ Logo with subtitle visible
├─ All menu items visible
├─ Language text + icon
├─ Full spacing
└─ No hamburger menu

TABLET (768-1199px):
├─ Logo subtitle hidden
├─ All menu items visible
├─ Language text + icon
├─ Reduced spacing
└─ No hamburger menu

MOBILE (<768px):
├─ Logo subtitle hidden
├─ Hamburger menu activated
├─ Language icon only
├─ Mobile dropdown menu
└─ Full-width touch targets
```

## 🎯 Hover States

```
LINK DEFAULT:
- Color: White
- Background: Transparent
- Underline: 0%
- Transform: translateY(0)

LINK HOVER:
- Color: White (same)
- Background: rgba(255,255,255,0.15)
- Underline: 80%
- Transform: translateY(-2px)

CONTACT LINK DEFAULT:
- Border: 2px rgba(255,255,255,0.5)
- Background: rgba(255,255,255,0.25)
- Color: White

CONTACT LINK HOVER:
- Border: 2px #ffd700
- Background: rgba(255,255,255,0.35)
- Color: #ffd700
- Shadow: 0 4px 12px rgba(255,215,0,0.3)

LOGO ICON HOVER:
- Transform: rotate(10deg) scale(1.1)
- Background: rgba(255,255,255,0.3)

LANGUAGE BUTTON DEFAULT:
- Background: rgba(255,255,255,0.25)
- Border: 2px rgba(255,255,255,0.4)
- Color: White

LANGUAGE BUTTON HOVER:
- Background: rgba(255,255,255,0.35)
- Border: 2px #ffd700
- Color: #ffd700
- Icon: rotate(20deg)
- Shadow: 0 4px 12px rgba(255,215,0,0.2)
- Transform: scale(1.05)
```

## 🔧 CSS Classes Reference

```
NAV STRUCTURE:
.navbar              ← Main nav element
.nav-container      ← Flex container
.nav-logo-section   ← Logo wrapper
.nav-logo           ← Logo flex layout
.logo-icon          ← Animated icon box
.logo-text          ← Text container
.logo-main          ← Main text
.logo-sub           ← Subtitle

MENU:
.nav-menu           ← Menu list
.nav-item           ← List item
.nav-link           ← Link element
.nav-contact        ← Contact link (special)

BUTTONS:
.nav-right          ← Right section
.lang-toggle-btn    ← Language button
.lang-text          ← Language text

MOBILE:
.hamburger          ← Hamburger icon
.hamburger.active   ← Active state (X)

STATE:
.navbar.scrolled    ← Scrolled navbar
.nav-menu.active    ← Active mobile menu
```

## 📋 JavaScript Functions

```
setLanguage(lang)
├─ Sets language (en/mr)
├─ Updates localStorage
├─ Calls updateAllText()
└─ Updates button text

setupEventListeners()
├─ Language toggle listener
└─ (Existing functionality)

setupNavbarScroll()
├─ Listens to scroll
├─ At scrollY > 50px
├─ Adds "scrolled" class
└─ Passive listener

setupMobileNavigation()
├─ Hamburger toggle
├─ Menu item clicks → close
├─ Outside click → close
└─ Manage active states
```

## ✨ Key Features Checklist

### Logo
- [ ] Icon in circular box
- [ ] Icon rotates on hover
- [ ] 2-line text
- [ ] Subtitle on desktop only

### Navigation
- [ ] Links centered
- [ ] Animated gold underlines
- [ ] White hover background
- [ ] Smooth transitions

### Contact
- [ ] Special border styling
- [ ] Gold text on hover
- [ ] Glow shadow effect

### Language
- [ ] Globe icon
- [ ] Glassmorphic background
- [ ] Icon rotates on hover
- [ ] Text hidden on mobile

### Scroll
- [ ] Darker gradient
- [ ] Enhanced shadow
- [ ] Smooth transition
- [ ] At 50px threshold

### Mobile
- [ ] Hamburger menu
- [ ] Animated lines to X
- [ ] Full-width dropdown
- [ ] Auto-close
```

## 🚀 Performance Tips

```
✅ GPU ACCELERATED (CSS Transform):
  - rotate()
  - scale()
  - translate()

❌ AVOID (CPU intensive):
  - left/right properties
  - width/height changes
  - margin/padding changes

✅ OPTIMIZATIONS:
  - Passive scroll listener
  - No heavy computations
  - Minimal DOM access
  - No reflows on animation
```

## 📚 File Reference

```
index.html
├─ Lines 18-54: Navbar HTML
└─ Updated structure + styles

contact.html
├─ Lines 11-44: Navbar HTML
└─ Same as index.html

css/styles.css
├─ Lines 50-217: Navbar CSS (NEW)
├─ Lines 758-847: Media queries (UPDATED)
└─ Added webkit compatibility

js/script.js
├─ Lines 1-51: Language setup (UPDATED)
├─ Lines 56-100: setupNavbarScroll() (NEW)
├─ Lines 102-130: setupMobileNavigation() (NEW)
└─ Lines 340-385: Page initialization
```

## 🎓 Customization Template

```
CHANGE LOGO TEXT:
<span class="logo-main" data-en="Your Name" data-mr="तुमचे नाव">
<span class="logo-sub" data-en="Your Tagline" data-mr="तुमचे टॅगलाइन">

CHANGE COLORS:
--primary-green: #your-color;
--light-green: #your-color;

CHANGE LINK SPEED:
transition: all 0.5s ease; /* Was 0.3s */

CHANGE UNDERLINE WIDTH:
width: 50%; /* Was 80% */

ADD MENU ITEM:
<li class="nav-item">
  <a href="#" class="nav-link" data-en="Text" data-mr="मजकूर">

CHANGE ANIMATION TIMING:
duration: 0.5s; /* Was 0.3s */
```

## 🔗 Useful Resources

```
Documentation Files:
✓ README.md - Complete guide
✓ CUSTOMIZATION.md - How to customize
✓ NAVBAR_IMPROVEMENTS.md - Features
✓ NAVBAR_BEFORE_AFTER.md - Comparison
✓ NAVBAR_VISUAL_GUIDE.md - Design
✓ NAVBAR_DEPLOYMENT.md - Deployment
✓ NAVBAR_QUICK_START.md - Quick start
```

## ✅ Quick Checklist

```
Before Deployment:
- [ ] Navbar displays correctly
- [ ] Logo shows properly
- [ ] Links are clickable
- [ ] Hover effects work
- [ ] Language toggle works
- [ ] Mobile menu opens/closes
- [ ] Scroll effect works
- [ ] No console errors
- [ ] All links navigate
- [ ] Mobile responsive
```

---

**Quick Reference Version**: 1.0
**Last Updated**: January 11, 2026
**Status**: ✅ Complete
