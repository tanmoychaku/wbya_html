import re

HTML = """
          <!-- Up to 14 Boys -->
          <div class="category-card">
            <h3 class="category-title">UP TO 14 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Roubhya Sankar Aluni</div></div>
              </div>
            </div>
          </div>

          <!-- Up to 14 Girls -->
          <div class="category-card">
            <h3 class="category-title">UP TO 14 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Ivy Sharma</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 18 Boys -->
          <div class="category-card">
            <h3 class="category-title">14 TO 18 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Arindam Nath</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 18 Girls -->
          <div class="category-card">
            <h3 class="category-title">14 TO 18 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Jolly Kundu</div></div>
              </div>
            </div>
          </div>

          <!-- 18 to 24 Men -->
          <div class="category-card">
            <h3 class="category-title">18 TO 24 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Pallab Dasgupta</div></div>
              </div>
            </div>
          </div>

          <!-- 18 to 24 Women -->
          <div class="category-card">
            <h3 class="category-title">18 TO 24 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Iti Sharma</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 30 Men -->
          <div class="category-card">
            <h3 class="category-title">24 TO 30 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Subodh Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Pradip Gupta</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 30 Women -->
          <div class="category-card">
            <h3 class="category-title">24 TO 30 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Ujjala Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Snigdha Sen</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Minakshi Sinha</div></div>
              </div>
            </div>
          </div>
"""

with open('results-10th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-10th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
