import re

new_articles = """
<!-- Favorite Card 4 -->
<article class="bg-surface rounded-2xl p-6 ambient-shadow hover:-translate-y-2 hover:shadow-lg transition-all duration-300 flex flex-col items-center text-center group">
<div class="w-full h-40 rounded-xl overflow-hidden mb-6 relative">
<img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="images/farm_fresh.png"/>
</div>
<h3 class="font-headline-md text-headline-md text-primary mb-2">Green Goddess</h3>
<div class="flex items-center justify-center gap-1 mb-3 text-secondary-fixed-dim">
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="text-on-surface-variant text-xs ml-1">(5.0)</span>
</div>
<p class="font-body-md text-body-md text-on-surface-variant mb-4 flex-grow">Spinach, Kale, Apple, Lemon, Ginger, Agave.</p>
<div class="w-full flex items-center justify-between mt-auto">
<span class="font-headline-md text-[20px] font-bold text-on-surface">$10.50</span>
<button class="bg-primary-container text-on-primary-container px-5 py-2 rounded-lg font-label-md text-label-md hover:bg-primary hover:text-on-primary transition-colors flex items-center gap-2">
                            Add <span class="material-symbols-outlined text-[18px]" data-icon="add_shopping_cart">add_shopping_cart</span>
</button>
</div>
</article>
<!-- Favorite Card 5 -->
<article class="bg-surface rounded-2xl p-6 ambient-shadow hover:-translate-y-2 hover:shadow-lg transition-all duration-300 flex flex-col items-center text-center group">
<div class="w-full h-40 rounded-xl overflow-hidden mb-6 relative">
<img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="images/zero_preservatives.png"/>
</div>
<h3 class="font-headline-md text-headline-md text-primary mb-2">Citrus Sunrise</h3>
<div class="flex items-center justify-center gap-1 mb-3 text-secondary-fixed-dim">
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star_half">star_half</span>
<span class="text-on-surface-variant text-xs ml-1">(4.7)</span>
</div>
<p class="font-body-md text-body-md text-on-surface-variant mb-4 flex-grow">Orange, Grapefruit, Lemon, Carrot, Turmeric.</p>
<div class="w-full flex items-center justify-between mt-auto">
<span class="font-headline-md text-[20px] font-bold text-on-surface">$9.00</span>
<button class="bg-primary-container text-on-primary-container px-5 py-2 rounded-lg font-label-md text-label-md hover:bg-primary hover:text-on-primary transition-colors flex items-center gap-2">
                            Add <span class="material-symbols-outlined text-[18px]" data-icon="add_shopping_cart">add_shopping_cart</span>
</button>
</div>
</article>
<!-- Favorite Card 6 -->
<article class="bg-surface rounded-2xl p-6 ambient-shadow hover:-translate-y-2 hover:shadow-lg transition-all duration-300 flex flex-col items-center text-center group">
<div class="w-full h-40 rounded-xl overflow-hidden mb-6 relative">
<img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="images/starter_kit.png"/>
</div>
<h3 class="font-headline-md text-headline-md text-primary mb-2">Berry Blast</h3>
<div class="flex items-center justify-center gap-1 mb-3 text-secondary-fixed-dim">
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="material-symbols-outlined fill-icon text-sm" data-icon="star">star</span>
<span class="text-on-surface-variant text-xs ml-1">(4.9)</span>
</div>
<p class="font-body-md text-body-md text-on-surface-variant mb-4 flex-grow">Strawberries, Blueberries, Raspberries, Acai, Apple.</p>
<div class="w-full flex items-center justify-between mt-auto">
<span class="font-headline-md text-[20px] font-bold text-on-surface">$10.00</span>
<button class="bg-primary-container text-on-primary-container px-5 py-2 rounded-lg font-label-md text-label-md hover:bg-primary hover:text-on-primary transition-colors flex items-center gap-2">
                            Add <span class="material-symbols-outlined text-[18px]" data-icon="add_shopping_cart">add_shopping_cart</span>
</button>
</div>
</article>
"""

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''</button>
</div>
</article>
</div>
</section>'''

replacement = f'''</button>
</div>
</article>
{new_articles}
</div>
</section>'''

if target in content:
    content = content.replace(target, replacement)
    with open('menu.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added articles successfully.")
else:
    print("Target not found.")
