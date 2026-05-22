import re

HTML = """
          <!-- 8 to 12 Boys -->
          <div class="category-card">
            <h3 class="category-title">8 TO 12 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Subhrojyoti Banik</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Subhasish Mondal</div></div>
              </div>
            </div>
          </div>

          <!-- 8 to 12 Girls -->
          <div class="category-card">
            <h3 class="category-title">8 TO 12 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumdar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Dayeta Sarkar</div></div>
              </div>
            </div>
          </div>

          <!-- 12 to 17 Boys (Typo in original HTML) -->
          <div class="category-card">
            <h3 class="category-title">12 TO 17 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sayani Mallick</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sreya Das</div></div>
              </div>
            </div>
          </div>

          <!-- 17 to 21 Girls -->
          <div class="category-card">
            <h3 class="category-title">17 TO 21 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Tania Nag</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Men -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Brajanath Basak</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Tapas Paul</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Women -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Manasi Manna</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Madhabi Seth</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 40 Men -->
          <div class="category-card">
            <h3 class="category-title">25 TO 40 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sourav Sekhar Kundu</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sanat Halder</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Ranjit Chakraborty</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 40 Women -->
          <div class="category-card">
            <h3 class="category-title">25 TO 40 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Kabita Dam</div></div>
              </div>
            </div>
          </div>

          <!-- 40 to 60 Women -->
          <div class="category-card">
            <h3 class="category-title">40 TO 60 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Chitra Banerjee</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Yoga (JR) Single -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC YOGA (JR) SINGLE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Nabomita Dasgupta</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Yoga (SR) Single -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC YOGA (SR) SINGLE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Madhabi Seth</div></div>
              </div>
            </div>
          </div>

          <!-- Rhythmic Yoga (JR) Pair -->
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC YOGA (JR) PAIR</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sreya Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumdar</div></div>
              </div>
            </div>
          </div>
"""

with open('results-36th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-36th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
