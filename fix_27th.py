import re

HTML = """
          <!-- 8 to 11 Boys -->
          <div class="category-card">
            <h3 class="category-title">8 TO 11 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Debayan Mitra</div></div>
              </div>
            </div>
          </div>

          <!-- 8 to 11 Girls -->
          <div class="category-card">
            <h3 class="category-title">8 TO 11 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sayona Das</div></div>
              </div>
            </div>
          </div>

          <!-- 11 to 14 Boys -->
          <div class="category-card">
            <h3 class="category-title">11 TO 14 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Pritam Pal</div></div>
              </div>
            </div>
          </div>

          <!-- 11 to 14 Girls -->
          <div class="category-card">
            <h3 class="category-title">11 TO 14 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Rupa Manna</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Madhumita Pal</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 17 Boys -->
          <div class="category-card">
            <h3 class="category-title">14 TO 17 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Brajanath Basak</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 17 Girls -->
          <div class="category-card">
            <h3 class="category-title">14 TO 17 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Mitrali Chakraborty</div></div>
              </div>
            </div>
          </div>

          <!-- 17 to 21 Girls -->
          <div class="category-card">
            <h3 class="category-title">17 TO 21 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Biswarupa Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Men -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Jhantu Roy</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Abhijit Sil</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Women -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Pratima Das</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 35 Men -->
          <div class="category-card">
            <h3 class="category-title">25 TO 35 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Somnath Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sudin Dhara</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 35 Women -->
          <div class="category-card">
            <h3 class="category-title">25 TO 35 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sankari Sanati</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Pampa Manna</div></div>
              </div>
            </div>
          </div>

          <!-- 35 to 45 Women -->
          <div class="category-card">
            <h3 class="category-title">35 TO 45 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Kumkum Sinha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Bandana Kumar</div></div>
              </div>
            </div>
          </div>

          <!-- Above 45 Men -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 45 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Parashuram Singh</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Amal Kumar Sain</div></div>
              </div>
            </div>
          </div>

          <!-- Above 45 Women -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 45 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sabita Banerjee</div></div>
              </div>
            </div>
          </div>
"""

with open('results-27th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-27th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
