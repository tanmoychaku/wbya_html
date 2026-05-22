import re

HTML = """
          <!-- Up to 12 Boys -->
          <div class="category-card">
            <h3 class="category-title">UP TO 12 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Kingsukh Lahiri</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Mayukh Das</div></div>
              </div>
            </div>
          </div>

          <!-- Up to 12 Girls -->
          <div class="category-card">
            <h3 class="category-title">UP TO 12 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Dipannita Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Antara Chowdhury</div></div>
              </div>
            </div>
          </div>

          <!-- 12 to 15 Boys -->
          <div class="category-card">
            <h3 class="category-title">12 TO 15 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Partha Sen</div></div>
              </div>
            </div>
          </div>

          <!-- 12 to 15 Girls -->
          <div class="category-card">
            <h3 class="category-title">12 TO 15 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Munmun Singha</div></div>
              </div>
            </div>
          </div>

          <!-- 18 to 21 Boys -->
          <div class="category-card">
            <h3 class="category-title">18 TO 21 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Arindam Nath</div></div>
              </div>
            </div>
          </div>

          <!-- 18 to 21 Girls -->
          <div class="category-card">
            <h3 class="category-title">18 TO 21 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Barnali Ghosh</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 24 Men -->
          <div class="category-card">
            <h3 class="category-title">21 TO 24 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Pallab Dasgupta</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 24 Women -->
          <div class="category-card">
            <h3 class="category-title">21 TO 24 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Uma Ghosh</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Basanti Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 28 Women -->
          <div class="category-card">
            <h3 class="category-title">24 TO 28 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Minakshi Sinha</div></div>
              </div>
            </div>
          </div>

          <!-- 28 to 35 Men -->
          <div class="category-card">
            <h3 class="category-title">28 TO 35 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Ashok Paul</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Pradeep Kumar</div></div>
              </div>
            </div>
          </div>

          <!-- 24 to 30 Women -->
          <div class="category-card">
            <h3 class="category-title">24 TO 30 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Dipika Bhattacharjee</div></div>
              </div>
            </div>
          </div>

          <!-- Above 45 Men -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 45 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Tapan Singh</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Niranjan Karak</div></div>
              </div>
            </div>
          </div>
"""

with open('results-12th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-12th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
