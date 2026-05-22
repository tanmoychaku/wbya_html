import re

HTML = """
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
                <div class="winner-info"><div class="winner-name">Piyasi Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Paromita Mondal</div></div>
              </div>
            </div>
          </div>

          <!-- 8 to 11 Boys -->
          <div class="category-card">
            <h3 class="category-title">8 TO 11 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Sayan Ghosh</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Arkaprova Banerjee</div></div>
              </div>
            </div>
          </div>

          <!-- 11 to 14 Girls -->
          <div class="category-card">
            <h3 class="category-title">11 TO 14 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Sakshi Dutta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Asmita Banerjee</div></div>
              </div>
            </div>
          </div>

          <!-- 11 to 14 Boys -->
          <div class="category-card">
            <h3 class="category-title">11 TO 14 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Prabuddha Dutta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Saibal Guchait</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
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
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Subhashree Basu</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 17 Boys -->
          <div class="category-card">
            <h3 class="category-title">14 TO 17 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Subhasis Mondal</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Ujjwal Pal</div></div>
              </div>
            </div>
          </div>

          <!-- 17 to 21 Girls -->
          <div class="category-card">
            <h3 class="category-title">17 TO 21 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Prakriti Barua</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Doli Panda</div></div>
              </div>
            </div>
          </div>

          <!-- 17 to 21 Boys -->
          <div class="category-card">
            <h3 class="category-title">17 TO 21 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Raju Kumar Das</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Women -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Madhubanti Dey</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Rakhi Chatterjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Bhagyashree Maity</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Men -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Mohan Kr. Singh</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Snehasish Malodas</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 35 Women -->
          <div class="category-card">
            <h3 class="category-title">25 TO 35 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Madhabi Seth</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Dolan Manna</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Manasi Manna</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 35 Men -->
          <div class="category-card">
            <h3 class="category-title">25 TO 35 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Binoy Paul</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Tapas Paul</div></div>
              </div>
            </div>
          </div>

          <!-- Above 35 Yrs Women -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 35 YRS WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Chitra Banerjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sonali Ghosh Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- Above 35 Yrs Men -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 35 YRS MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Manas Nukherjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Tapan Nath</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Pijush Kanti Pan</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic JR Boys Single -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC JR BOYS SINGLE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Probuddha Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic JR Girls Single -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC JR GIRLS SINGLE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Dayeta Sarkar</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic SR Women Single -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC SR WOMEN SINGLE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Madhabi Seth</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic JR Pair -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC JR PAIR</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Asmita Banerjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Dayeta Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Subhasree</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic SR Pair -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC SR PAIR</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Tapas Paul</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Rakhi Chatterjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Madhabi Seth</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Madhubanti Dey</div></div>
              </div>
            </div>
          </div>

          <!-- Rhythmic Yoga JR -->
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC YOGA JR</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Probuddha Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- Rhythmic Yoga SR -->
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC YOGA SR</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Madhabi Seth</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Madhubanti Dey</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Rakhi Chatterjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Bhagyashree Maity</div></div>
              </div>
            </div>
          </div>
"""

with open('results-39th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-39th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
