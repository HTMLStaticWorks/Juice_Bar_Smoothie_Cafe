from bs4 import BeautifulSoup
import os

new_footer_html = """
<footer class="bg-surface-container-low dark:bg-surface-container border-t border-outline-variant dark:border-on-surface-variant/20 w-full pt-16 pb-8 px-margin-mobile md:px-margin-desktop mt-auto">
    <div class="max-w-container-max mx-auto grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
        <div class="flex flex-col items-start text-left">
            <a href="index.html" class="font-headline-md text-headline-md font-bold text-primary dark:text-primary-fixed-dim flex items-center gap-2 mb-4 hover:scale-105 transition-transform duration-200">
                <span class="material-symbols-outlined text-primary dark:text-primary-fixed-dim" style="font-variation-settings: 'FILL' 1;">local_drink</span>
                ZestUp
            </a>
            <p class="font-body-md text-body-md text-on-surface-variant dark:text-outline-variant mb-6">Crafting wellness, one sip at a time.</p>
            <div class="flex items-center gap-4">
                <a href="#" class="w-10 h-10 rounded-full bg-surface-variant dark:bg-on-surface-variant/20 flex items-center justify-center text-on-surface-variant hover:bg-primary hover:text-on-primary transition-colors">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                </a>
                <a href="#" class="w-10 h-10 rounded-full bg-surface-variant dark:bg-on-surface-variant/20 flex items-center justify-center text-on-surface-variant hover:bg-primary hover:text-on-primary transition-colors">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                </a>
            </div>
        </div>

        <div class="flex flex-col items-start">
            <h4 class="font-label-md text-label-md text-on-surface dark:text-inverse-surface font-bold mb-6 uppercase tracking-wider">Quick Links</h4>
            <ul class="flex flex-col gap-4 font-body-md text-body-md w-full">
                <li><a href="index.html" class="footer-link">Home</a></li>
                <li><a href="menu.html" class="footer-link">Menu</a></li>
                <li><a href="services.html" class="footer-link">Services</a></li>
                <li><a href="gallery.html" class="footer-link">Gallery</a></li>
            </ul>
        </div>

        <div class="flex flex-col items-start">
            <h4 class="font-label-md text-label-md text-on-surface dark:text-inverse-surface font-bold mb-6 uppercase tracking-wider">Company</h4>
            <ul class="flex flex-col gap-4 font-body-md text-body-md w-full">
                <li><a href="about.html" class="footer-link">Home 2</a></li>
                <li><a href="blog.html" class="footer-link">Blog</a></li>
                <li><a href="contact.html" class="footer-link">Contact Us</a></li>
            </ul>
        </div>

        <div class="flex flex-col items-start">
            <h4 class="font-label-md text-label-md text-on-surface dark:text-inverse-surface font-bold mb-6 uppercase tracking-wider">Stay Refreshed</h4>
            <p class="font-body-md text-body-md text-on-surface-variant dark:text-outline-variant mb-4">Subscribe to our newsletter for the latest recipes and exclusive offers.</p>
            <form class="w-full flex gap-2">
                <input type="email" placeholder="Your email" class="w-full px-4 py-3 rounded-lg border-2 border-outline-variant bg-surface dark:bg-surface-container-highest focus:border-primary focus:ring-0 transition-colors font-body-md text-body-md outline-none" required>
                <button type="submit" class="bg-primary text-on-primary px-6 py-3 rounded-lg font-label-md font-bold hover:scale-105 transition-transform duration-200">
                    <span class="material-symbols-outlined text-[20px]">send</span>
                </button>
            </form>
        </div>
    </div>

    <div class="max-w-container-max mx-auto border-t border-outline-variant dark:border-on-surface-variant/20 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="font-label-md text-label-md text-on-surface-variant/70 dark:text-outline-variant/70 text-center md:text-left">
            &copy; 2026 ZestUp. All rights reserved.
        </p>
        <div class="flex items-center gap-6">
            <a href="index.html" class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary transition-colors">Privacy Policy</a>
            <a href="index.html" class="font-label-md text-label-md text-on-surface-variant dark:text-outline-variant hover:text-primary transition-colors">Terms of Service</a>
        </div>
    </div>
</footer>
"""

files = ['index.html', 'menu.html', 'services.html', 'about.html', 'gallery.html', 'blog.html', 'contact.html']

for filename in files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    old_footer = soup.find('footer')
    if old_footer:
        import copy
        new_f_soup = BeautifulSoup(new_footer_html, 'html.parser')
        
        # Determine active highlight
        for a in new_f_soup.find_all('a', class_='footer-link'):
            href = a.get('href')
            if href == filename:
                a['class'] = "text-primary dark:text-primary-fixed-dim font-bold border-l-2 border-primary pl-3 block w-full text-left transition-colors".split()
            else:
                a['class'] = "text-on-surface-variant dark:text-outline-variant hover:text-primary dark:hover:text-primary-fixed-dim transition-colors block w-full text-left border-l-2 border-transparent pl-3".split()
                
        old_footer.replace_with(new_f_soup)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup).replace("</main></body></html>", "\n</main>\n</body>\n</html>"))

print("Footer redesigned across all pages.")
