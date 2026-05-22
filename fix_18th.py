import re

HTML = """
          <!-- 8 to 12 Boys -->
          <div class="category-card">
            <h3 class="category-title">8 TO 12 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Biswajit Nandi</div></div>
              </div>
            </div>
          </div>

          <!-- 8 to 12 Girls -->
          <div class="category-card">
            <h3 class="category-title">8 TO 12 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Kankana Sinha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Saheli Ganguly</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Kasturi Banerjee</div></div>
              </div>
            </div>
          </div>

          <!-- 12 to 15 Girls -->
          <div class="category-card">
            <h3 class="category-title">12 TO 15 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sumana Dey</div></div>
              </div>
            </div>
          </div>

          <!-- 15 to 19 Boys -->
          <div class="category-card">
            <h3 class="category-title">15 TO 19 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Somnath Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- 15 to 19 Girls -->
          <div class="category-card">
            <h3 class="category-title">15 TO 19 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Antara Chowdhury</div></div>
              </div>
            </div>
          </div>

          <!-- 19 to 24 Women -->
          <div class="category-card">
            <h3 class="category-title">19 TO 24 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sikha Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Kakoli Koley</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Santana Bag</div></div>
              </div>
            </div>
          </div>

          <!-- 19 to 24 Men -->
          <div class="category-card">
            <h3 class="category-title">19 TO 24 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Partha Sen</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 30 Men -->
          <div class="category-card">
            <h3 class="category-title">24 TO 30 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Manoj Khan</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Avijit Chakraborty</div></div>
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
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Pallab Dasgupta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sajal Mitra</div></div>
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
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Bandana Kumar</div></div>
              </div>
            </div>
          </div>
"""

with open('results-18th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-18th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
