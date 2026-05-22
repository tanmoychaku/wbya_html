import re

HTML = """
          <!-- Up to 12 Boys -->
          <div class="category-card">
            <h3 class="category-title">UP TO 12 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Suman Chaudhury</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Saikat Roy</div></div>
              </div>
            </div>
          </div>

          <!-- Up to 12 Girls -->
          <div class="category-card">
            <h3 class="category-title">UP TO 12 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Malatika Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Chaitali Bhattacharya</div></div>
              </div>
            </div>
          </div>

          <!-- 12 to 18 Girls -->
          <div class="category-card">
            <h3 class="category-title">12 TO 18 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Rajashree Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Iti Sarma</div></div>
              </div>
            </div>
          </div>

          <!-- Men -->
          <div class="category-card">
            <h3 class="category-title">MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Ashim Ghosal</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Dipak Kundu</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Subir Roy</div></div>
              </div>
            </div>
          </div>

          <!-- Women 1 -->
          <div class="category-card">
            <h3 class="category-title">WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Ujjala Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Debasree Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- Women 2 -->
          <div class="category-card">
            <h3 class="category-title">WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Lolita Polley</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Bulu Dev</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Santi Adhikary</div></div>
              </div>
            </div>
          </div>
"""

with open('results-5th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-5th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
