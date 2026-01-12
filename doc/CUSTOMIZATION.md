# 🎯 Quick Start & Customization Guide

## 🚀 Quick Start (5 Minutes)

### Step 1: Open the Website
1. Navigate to your project folder
2. Double-click `index.html` to open in browser
3. Or use: `http://localhost:8000` if using a local server

### Step 2: Test All Features
- Click "मराठी" button to switch to Marathi
- Use hamburger menu on mobile
- Scroll down to see animations
- Click "Contact" in navigation
- Test WhatsApp button

## 🎨 Customization Guide

### 1. Change Farmer Information

**File:** `contact.html` and `index.html` (footer section)

```html
<!-- Change farmer name -->
<p id="farmer-name">आपला नाव / Your Name</p>

<!-- Change phone -->
<a href="tel:+919876543210">+91 XXXXX XXXXX</a>

<!-- Change WhatsApp -->
<button class="whatsapp-btn" onclick="openWhatsApp('91XXXXXXXXXX')">
```

**Also update in:** `js/script.js` - WhatsApp phone number function calls

### 2. Change Colors

**File:** `css/styles.css` (at the top)

```css
:root {
    --primary-green: #2d6a4f;      /* Main brand color */
    --light-green: #40916c;        /* Secondary color */
    --accent-green: #52b788;       /* Accent color */
    --earthy-brown: #8b6f47;       /* Text color */
    /* ... update other colors ... */
}
```

### 3. Add/Edit Crops

**File:** `index.html` (Crops Section)

```html
<!-- Find the crops section and copy a crop-card template -->
<div class="crop-card">
    <div class="crop-image">
        <img src="YOUR_IMAGE_URL" alt="Crop Name">
    </div>
    <div class="crop-info">
        <h3 data-en="Crop Name" data-mr="क्रॉप नाव">Crop Name</h3>
        <div class="crop-details">
            <p><strong data-en="Season:" data-mr="ऋतु:">Season:</strong> 
               <span data-en="Jan - Mar" data-mr="जान - मार्च">Jan - Mar</span></p>
            <p><strong data-en="Benefits:" data-mr="फायदे:">Benefits:</strong> 
               <span data-en="Your benefits here" data-mr="आपले फायदे">Benefits here</span></p>
            <p><strong data-en="Method:" data-mr="पद्धती:">Method:</strong> 
               <span data-en="Your method" data-mr="आपली पद्धती">Method here</span></p>
        </div>
    </div>
</div>
```

### 4. Change Contact Information

**File:** `contact.html`

```html
<!-- Change location -->
<p data-en="Phaltan, Satara District, Maharashtra" 
   data-mr="फलटण, सातारा जिल्हा, महाराष्ट्र">
   Your Location
</p>

<!-- Change Google Maps coordinates -->
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12...">
```

### 5. Change Website Logo/Title

**File:** `index.html` and `contact.html`

```html
<div class="nav-logo">
    <i class="fas fa-leaf"></i>  <!-- Change this icon -->
    <span id="logo-text">Your Farm Name</span>
</div>

<!-- Also change in title -->
<title>Your Farm Name - Organic Agriculture</title>
```

### 6. Update Social Media Links

**File:** `index.html` and `contact.html` (Footer)

```html
<div class="social-links">
    <a href="https://facebook.com/yourpage">
        <i class="fab fa-facebook"></i>
    </a>
    <!-- Update href with your social links -->
</div>
```

### 7. Replace Placeholder Images

**All images use placeholder URLs:**

```html
<!-- Current: -->
<img src="https://placehold.co/600x400?text=Organic+Farm" 
     alt="Organic Farming">

<!-- Replace with your actual image: -->
<img src="images/farm.jpg" alt="Organic Farming">
```

**Recommended Image Sizes:**
- Hero: 600x400px
- Crops: 300x250px
- Gallery: 300x300px
- Thumbnails: 150x150px

### 8. Add Your Own Services

**File:** `index.html` (Services Section)

```html
<div class="service-card">
    <div class="service-icon">
        <i class="fas fa-icon-name"></i>  <!-- Font Awesome icon -->
    </div>
    <h3 data-en="Service Name" data-mr="सेवा नाव">Service Name</h3>
    <p data-en="Service description in English" 
       data-mr="मराठीत सेवाचे वर्णन">
        Service description
    </p>
</div>
```

**Available Font Awesome Icons:**
- `fa-flask-vial` - Lab/Testing
- `fa-water` - Water
- `fa-leaf` - Leaf/Plant
- `fa-bug` - Pest
- `fa-tree` - Tree
- Find more at: [Font Awesome Icons](https://fontawesome.com/icons)

### 9. Customize Bilingual Text

**How to add translations:**

Every text element uses:
```html
<h1 data-en="English Text" data-mr="मराठी मजकूर">English Text</h1>
```

**Steps:**
1. Copy the English text as `data-en` value
2. Translate to Marathi as `data-mr` value
3. Display text is whatever appears between the tags

### 10. Enable Email Notifications (Optional)

To send emails from contact form:

#### Option A: Formspree (Easiest)
1. Go to [formspree.io](https://formspree.io)
2. Sign up and create a form
3. Get your form ID
4. Update in `contact.html`:

```html
<form id="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

#### Option B: Create Backend
1. Create a `handler.php` or `handler.py`
2. Update form action
3. Process and send emails

### 11. Customize Contact Form

**File:** `contact.html`

Add more form fields:

```html
<div class="form-group">
    <label for="field-name" data-en="Label" data-mr="लेबल">Label</label>
    <input type="type" id="field-name" name="field-name" required>
</div>
```

Change subject options:

```html
<select id="subject" name="subject" required>
    <option value="" data-en="Select a subject" data-mr="विषय निवडा">
        Select a subject
    </option>
    <option value="new-topic" data-en="New Topic" data-mr="नवीन विषय">
        New Topic
    </option>
</select>
```

## 📱 Mobile Testing

### Test on Different Devices

1. **Chrome DevTools:**
   - Press `F12` to open
   - Click device toggle (Ctrl+Shift+M)
   - Test on iPhone, Android, iPad

2. **Real Device:**
   - Use `http://YOUR_IP:8000`
   - Scan QR code on mobile

## 🔐 Before Going Live

- [ ] Remove placeholder images
- [ ] Update all farmer information
- [ ] Change all placeholder phone numbers
- [ ] Update location in map
- [ ] Add social media links
- [ ] Test contact form submission
- [ ] Test WhatsApp integration
- [ ] Test language switching
- [ ] Test on mobile devices
- [ ] Enable HTTPS
- [ ] Add Google Analytics
- [ ] Create sitemap.xml
- [ ] Submit to Google Search Console

## 🚀 Deploying to Internet

### Option 1: Free Hosting (Netlify)
1. Push code to GitHub
2. Connect GitHub to Netlify
3. Auto-deploy on push
4. Get free domain

### Option 2: GitHub Pages
1. Push to GitHub
2. Enable GitHub Pages in settings
3. Access at `username.github.io/Agriculture_Project`

### Option 3: Web Host
1. Use: Bluehost, HostGator, GoDaddy, etc.
2. Upload files via FTP
3. Point domain to hosting

### Option 4: VPS/Cloud
1. AWS, Google Cloud, Heroku
2. Deploy using Git or Docker
3. Full control and scalability

## 📊 Adding Analytics

Add Google Analytics to track visitors:

```html
<!-- Add inside <head> in both HTML files -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

## 💡 Tips & Tricks

### 1. Keyboard Shortcuts
- `Alt + L` = Toggle language
- `Alt + T` = Back to top

### 2. Browser Console
Open DevTools (F12) → Console to see logs

### 3. Performance
- Compress images to < 100KB
- Use modern formats (WebP)
- Enable browser caching

### 4. SEO Improvements
- Add meta descriptions
- Create an XML sitemap
- Submit to Google Search Console
- Add backlinks from agricultural sites

### 5. Accessibility
- Use keyboard to navigate
- Test with screen readers
- Maintain color contrast

## 🐛 Troubleshooting

### Issue: Language not switching
**Solution:** Check browser localStorage is enabled

### Issue: Images not loading
**Solution:** Check image URLs are correct and accessible

### Issue: WhatsApp link not working
**Solution:** Verify phone number format (91 + 10 digits)

### Issue: Form not submitting
**Solution:** Check form action URL and method

### Issue: Styles not applying
**Solution:** Clear browser cache (Ctrl+Shift+Delete)

## 📚 Resources

- [Font Awesome Icons](https://fontawesome.com/icons)
- [Google Maps Embed](https://www.google.com/maps)
- [Formspree Forms](https://formspree.io)
- [HTML Reference](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)

## 📞 Support

If you need help:
1. Check the README.md
2. Check browser console for errors (F12)
3. Test in different browser
4. Clear cache and hard refresh (Ctrl+F5)

---

**Happy Farming! 🌱**

For questions: See README.md or check config.json for settings
