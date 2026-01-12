// ===========================
// LANGUAGE SWITCHING FUNCTIONALITY
// ===========================

const langToggleBtn = document.getElementById('lang-toggle');
const htmlTag = document.documentElement;
let currentLang = localStorage.getItem('lang') || 'en';

// Initialize language on page load
document.addEventListener('DOMContentLoaded', () => {
    setLanguage(currentLang);
    setupEventListeners();
    setupNavbarScroll();
    setupMobileNavigation();
});

// Set language for entire page
function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('lang', lang);

    if (lang === 'mr') {
        document.body.classList.add('marathi');
        htmlTag.lang = 'mr';
        const langText = document.querySelector('.lang-text');
        if (langText) langText.textContent = 'मराठी';
        updateAllText('mr');
    } else {
        document.body.classList.remove('marathi');
        htmlTag.lang = 'en';
        const langText = document.querySelector('.lang-text');
        if (langText) langText.textContent = 'English';
        updateAllText('en');
    }
}

// Update all text elements with language
function updateAllText(lang) {
    const elements = document.querySelectorAll('[data-en][data-mr]');
    elements.forEach(el => {
        if (lang === 'mr') {
            if (el.textContent.includes(el.getAttribute('data-en'))) {
                el.textContent = el.getAttribute('data-mr');
            }
        } else {
            if (el.textContent.includes(el.getAttribute('data-mr'))) {
                el.textContent = el.getAttribute('data-en');
            }
        }
    });
}

// Language toggle button
langToggleBtn.addEventListener('click', () => {
    const newLang = currentLang === 'en' ? 'mr' : 'en';
    setLanguage(newLang);
});

// ===========================
// NAVIGATION FUNCTIONALITY
// ===========================

const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

function setupEventListeners() {
    // Hamburger menu toggle
    hamburger.addEventListener('click', toggleMenu);

    // Close menu when nav link is clicked
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.navbar')) {
            navMenu.classList.remove('active');
        }
    });
}

function toggleMenu() {
    navMenu.classList.toggle('active');
}

// ===========================
// SMOOTH SCROLLING
// ===========================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===========================
// BACK TO TOP BUTTON
// ===========================

const backToTopBtn = document.getElementById('back-to-top');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        backToTopBtn.classList.add('show');
    } else {
        backToTopBtn.classList.remove('show');
    }
});

backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// ===========================
// INTERSECTION OBSERVER FOR ANIMATIONS
// ===========================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe cards for animation
document.querySelectorAll('.crop-card, .input-card, .service-card, .practice-card, .cert-card, .gallery-item').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(card);
});

// ===========================
// LAZY LOADING IMAGES
// ===========================

if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                img.classList.add('loaded');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img').forEach(img => {
        imageObserver.observe(img);
    });
}

// ===========================
// CONTACT FORM SUBMISSION (if on contact page)
// ===========================

const contactForm = document.getElementById('contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const formData = {
            name: document.getElementById('name').value,
            phone: document.getElementById('phone').value,
            email: document.getElementById('email').value,
            message: document.getElementById('message').value
        };

        // Validate form
        if (!formData.name || !formData.phone || !formData.email || !formData.message) {
            alert(currentLang === 'mr' ? 'कृपया सर्व फील्ड भरा' : 'Please fill all fields');
            return;
        }

        // Simulate form submission
        console.log('Form submitted:', formData);
        
        // Show success message
        const successMsg = currentLang === 'mr' 
            ? 'आपली संपर्क माहिती सफलतापूर्वक पाठवली गेली' 
            : 'Your message has been sent successfully';
        
        alert(successMsg);
        contactForm.reset();
    });
}

// ===========================
// WHATSAPP INTEGRATION
// ===========================

function openWhatsApp(phoneNumber, message = '') {
    const encodedMessage = encodeURIComponent(message || 'नमस्ते! मला आपल्या शेती सेवांबद्दल माहिती हवी आहे। / Hello! I would like to know more about your farming services.');
    const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
    window.open(whatsappUrl, '_blank');
}

// ===========================
// SCROLL ANIMATIONS
// ===========================

const animateOnScroll = () => {
    const elements = document.querySelectorAll('[data-animate]');
    
    elements.forEach(el => {
        const elementTop = el.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < window.innerHeight - elementVisible) {
            el.classList.add('animated');
        }
    });
};

window.addEventListener('scroll', animateOnScroll);
animateOnScroll(); // Run on initial load

// ===========================
// FORM VALIDATION
// ===========================

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePhone(phone) {
    const re = /^[6-9]\d{9}$/; // Indian phone number format
    return re.test(phone);
}

// ===========================
// SERVICE WORKER REGISTRATION (for offline support)
// ===========================

if ('serviceWorker' in navigator) {
    // Uncomment to enable service worker
    // navigator.serviceWorker.register('sw.js')
    //     .then(reg => console.log('Service Worker registered'))
    //     .catch(err => console.log('SW registration failed: ', err));
}

// ===========================
// PERFORMANCE OPTIMIZATION
// ===========================

// Debounce function for scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ===========================
// PRINT FUNCTIONALITY
// ===========================

function printPage() {
    window.print();
}

// ===========================
// KEYBOARD SHORTCUTS
// ===========================

document.addEventListener('keydown', (e) => {
    // Alt + L for language toggle
    if (e.altKey && e.key === 'l') {
        langToggleBtn.click();
    }
    
    // Alt + T for back to top
    if (e.altKey && e.key === 't') {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
});

// ===========================
// NAVBAR SCROLL EFFECT
// ===========================
function setupNavbarScroll() {
    const navbar = document.getElementById('navbar');
    let lastScrollY = 0;

    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;

        if (currentScrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        lastScrollY = currentScrollY;
    }, { passive: true });
}

// ===========================
// MOBILE NAVIGATION TOGGLE
// ===========================
function setupMobileNavigation() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close menu when a link is clicked
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-container')) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });
}

// ===========================
// PAGE PERFORMANCE MONITORING
// ===========================

if (window.performance && window.performance.timing) {
    window.addEventListener('load', () => {
        const perfData = window.performance.timing;
        const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log('Page load time: ' + pageLoadTime + 'ms');
    });
}

console.log('Green Farming Website Initialized');
console.log('Language: ' + currentLang);
console.log('Theme: Organic & Sustainable Agriculture');
