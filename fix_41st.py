import re

HTML = """
          <!-- 8 to 11 Girls -->
          <div class="category-card">
            <h3 class="category-title">8 TO 11 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Ishani Dey</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Pramita Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Prerana Mallick</div></div>
              </div>
            </div>
          </div>

          <!-- 8 to 11 Boys -->
          <div class="category-card">
            <h3 class="category-title">8 TO 11 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Ajoy Saren</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Debraj Shaw</div></div>
              </div>
            </div>
          </div>

          <!-- 11 to 14 Boys -->
          <div class="category-card">
            <h3 class="category-title">11 TO 14 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Avay Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sowel Ahmed Gazi</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Prabuddha Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 17 Girls -->
          <div class="category-card">
            <h3 class="category-title">14 TO 17 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Nabomita Dasgupta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumdar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
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
                <div class="winner-info"><div class="winner-name">Saibal Guchait</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Subhrajyoti Banik</div></div>
              </div>
            </div>
          </div>

          <!-- 17 to 21 Women -->
          <div class="category-card">
            <h3 class="category-title">17 TO 21 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Antara Dutta</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Women -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sanchaita Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Supriya Panda</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Supriti Pal</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Men -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 MEN</h3>
            <div class="winners-list">
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
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Dolon Manna</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Madhubanty Dey</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Nupur Debnath</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 35 Men -->
          <div class="category-card">
            <h3 class="category-title">25 TO 35 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Brajanath Basak</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Tapas Paul</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Binay Pal</div></div>
              </div>
            </div>
          </div>

          <!-- Above 35 Yrs Women -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 35 YRS WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Debjani Biswas Mondal</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Sonali Ghosh (Dutta)</div></div>
              </div>
            </div>
          </div>

          <!-- Above 35 Yrs Men -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 35 YRS MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Manas Mukherjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Pallab Das Gupta</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic JR Boys Single -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC JR BOYS SINGLE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Sowel Ahmed Gazi</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
              </div>
            </div>
          </div>

          <!-- Rhythmic SR Girls Pair -->
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC SR GIRLS PAIR</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Supriti Pal</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Madhubanty Dey</div></div>
              </div>
            </div>
          </div>

          <!-- Professional Group (Women) -->
          <div class="category-card">
            <h3 class="category-title">PROFESSIONAL GROUP (WOMEN)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Chitra Banerjee</div></div>
              </div>
            </div>
          </div>

          <!-- Professional Group (Men) -->
          <div class="category-card">
            <h3 class="category-title">PROFESSIONAL GROUP (MEN)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Amalendu Mondal</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Manik Pradhan</div></div>
              </div>
            </div>
          </div>
"""

with open('results-41st-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-41st-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
