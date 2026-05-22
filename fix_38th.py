import re

HTML = """
          <!-- 8 to 11 Boys -->
          <div class="category-card">
            <h3 class="category-title">8 TO 11 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Abhirup Bose</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Prabuddha Dutta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sayan Debnath</div></div>
              </div>
            </div>
          </div>

          <!-- 8 to 11 Girls -->
          <div class="category-card">
            <h3 class="category-title">8 TO 11 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Riya Paul</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Punam Karmakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Amisha Khan</div></div>
              </div>
            </div>
          </div>

          <!-- 11 to 14 Boys -->
          <div class="category-card">
            <h3 class="category-title">11 TO 14 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Saibal Guchait</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Subhrajyoti Banik</div></div>
              </div>
            </div>
          </div>

          <!-- 11 to 14 Girls -->
          <div class="category-card">
            <h3 class="category-title">11 TO 14 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Sakshi Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 17 Boys -->
          <div class="category-card">
            <h3 class="category-title">14 TO 17 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Subrata Mondal</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Debabrata Ghosh</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 17 Girls -->
          <div class="category-card">
            <h3 class="category-title">14 TO 17 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Dayeta Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Prakiti Barua</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Neha Shaw</div></div>
              </div>
            </div>
          </div>

          <!-- 17 to 21 Boys -->
          <div class="category-card">
            <h3 class="category-title">17 TO 21 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Raju Kumar Das</div></div>
              </div>
            </div>
          </div>

          <!-- 17 to 21 Girls -->
          <div class="category-card">
            <h3 class="category-title">17 TO 21 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Doly Panda</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Sreya Das</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Men -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Mohan Singh</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Women -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Tania Nag</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Dolan Manna</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Madhabi Seth</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 35 Men -->
          <div class="category-card">
            <h3 class="category-title">25 TO 35 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Binay Paul</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Tapas Paul</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sanat Halder</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 35 Women -->
          <div class="category-card">
            <h3 class="category-title">25 TO 35 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Manasi Manna</div></div>
              </div>
            </div>
          </div>

          <!-- Above 35 Men -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 35 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sourav Sekhar Kundu</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Manas Mukherjee</div></div>
              </div>
            </div>
          </div>

          <!-- Above 35 Women -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 35 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Papia Ganguly</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Chitra Banerjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sonali Ghosh (Dutta)</div></div>
              </div>
            </div>
          </div>
"""

with open('results-38th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-38th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
