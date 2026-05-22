import re

HTML = """
          <!-- Up to 14 Girls -->
          <div class="category-card">
            <h3 class="category-title">UP TO 14 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Soma Chatterjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Papita Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Anita Sen</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 18 Boys -->
          <div class="category-card">
            <h3 class="category-title">14 TO 18 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sabyasachi C</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Mintu Das</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 18 Girls -->
          <div class="category-card">
            <h3 class="category-title">14 TO 18 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Malatika Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Iti Sarma</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Santwana Sinha</div></div>
              </div>
            </div>
          </div>

          <!-- 18 to 24 Men -->
          <div class="category-card">
            <h3 class="category-title">18 TO 24 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Dipak Dey</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">B. Gopal Majumdar</div></div>
              </div>
            </div>
          </div>

          <!-- 18 to 24 Women -->
          <div class="category-card">
            <h3 class="category-title">18 TO 24 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Smriti Sarma</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Maya Kundu</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 30 Men -->
          <div class="category-card">
            <h3 class="category-title">24 TO 30 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Ambika Bhattacharjee</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 30 Women -->
          <div class="category-card">
            <h3 class="category-title">24 TO 30 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Shila Roy</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Anima Ghosh</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Bulu Dev</div></div>
              </div>
            </div>
          </div>

          <!-- Above 30 Women -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 30 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Santi Adhikari</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Uma Bhattacharjee</div></div>
              </div>
            </div>
          </div>
"""

with open('results-7th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-7th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
