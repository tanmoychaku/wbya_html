import re

HTML = """
          <!-- 8 to 12 Girls -->
          <div class="category-card">
            <h3 class="category-title">8 TO 12 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Aishali Guha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Ayanima Banerjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Moumita Das</div></div>
              </div>
            </div>
          </div>

          <!-- 8 to 12 Boys -->
          <div class="category-card">
            <h3 class="category-title">8 TO 12 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Koushik Bhattacharjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sayantan Dey</div></div>
              </div>
            </div>
          </div>

          <!-- 15 to 19 Boys -->
          <div class="category-card">
            <h3 class="category-title">15 TO 19 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sourav Sekhar Kundu</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Somnath Das</div></div>
              </div>
            </div>
          </div>

          <!-- 15 to 19 Girls -->
          <div class="category-card">
            <h3 class="category-title">15 TO 19 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Susmita Barua</div></div>
              </div>
            </div>
          </div>

          <!-- 19 to 24 Men -->
          <div class="category-card">
            <h3 class="category-title">19 TO 24 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Manas Mukherjee</div></div>
              </div>
            </div>
          </div>

          <!-- 19 to 24 Women -->
          <div class="category-card">
            <h3 class="category-title">19 TO 24 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Rinku Kar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Champa Das</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 30 Men -->
          <div class="category-card">
            <h3 class="category-title">24 TO 30 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Manoj Khan</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Dipesh Bhattacharya</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 30 Women -->
          <div class="category-card">
            <h3 class="category-title">24 TO 30 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Kumkum Sinha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Basanti Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- Above 30 Men -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 30 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Pallab Dasgupta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Anup Maity</div></div>
              </div>
            </div>
          </div>

          <!-- Above 30 Women -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 30 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Namita Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Beauti Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Bandana Kumar</div></div>
              </div>
            </div>
          </div>
"""

with open('results-19th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-19th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
