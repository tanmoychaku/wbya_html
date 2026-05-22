import re

HTML = """
          <!-- 8 to 12 Boys -->
          <div class="category-card">
            <h3 class="category-title">8 TO 12 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Aninda Banerjee</div></div>
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
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Trina Roy</div></div>
              </div>
            </div>
          </div>

          <!-- 12 to 15 Girls -->
          <div class="category-card">
            <h3 class="category-title">12 TO 15 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Moumita Bose</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Antara Chowdhury</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sutapa Karak</div></div>
              </div>
            </div>
          </div>

          <!-- 15 to 18 Girls -->
          <div class="category-card">
            <h3 class="category-title">15 TO 18 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Swati Mukherjee</div></div>
              </div>
            </div>
          </div>

          <!-- 18 to 21 Girls -->
          <div class="category-card">
            <h3 class="category-title">18 TO 21 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sikha Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sonali Das</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 24 Men -->
          <div class="category-card">
            <h3 class="category-title">21 TO 24 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Monoj Khan</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Nabakrishna Das</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 24 Women -->
          <div class="category-card">
            <h3 class="category-title">21 TO 24 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Madhumita Sen</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Rina Kar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Purabi Sharma</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 28 Women -->
          <div class="category-card">
            <h3 class="category-title">24 TO 28 WOMEN</h3>
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

          <!-- 28 to 35 Men -->
          <div class="category-card">
            <h3 class="category-title">28 TO 35 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Anup Kumar Maity</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Prasanta Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- 28 to 35 Women -->
          <div class="category-card">
            <h3 class="category-title">28 TO 35 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Uma Banerjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Neeti Sharma</div></div>
              </div>
            </div>
          </div>

          <!-- 35 to 45 Men -->
          <div class="category-card">
            <h3 class="category-title">35 TO 45 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Ram Chandra Naskar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Anuva Samanta</div></div>
              </div>
            </div>
          </div>

          <!-- Above 45 Men -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 45 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Lakshman Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Biswaprasad Dharchowdhury</div></div>
              </div>
            </div>
          </div>

          <!-- Above 45 Women -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 45 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Anjali Adhikary</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Shanta Krishnan</div></div>
              </div>
            </div>
          </div>
"""

with open('results-17th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-17th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
