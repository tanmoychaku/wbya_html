import re

HTML = """
          <!-- 8 to 11 Girls -->
          <div class="category-card">
            <h3 class="category-title">8 TO 11 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Payel Saha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Tanisha Das</div></div>
              </div>
            </div>
          </div>

          <!-- 8 to 11 Boys -->
          <div class="category-card">
            <h3 class="category-title">8 TO 11 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Manash Karmakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Debojyoti Pramanick</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Sougata Paul</div></div>
              </div>
            </div>
          </div>

          <!-- 11 to 14 Girls -->
          <div class="category-card">
            <h3 class="category-title">11 TO 14 GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Shubhrajyoti Mahalder</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Pratyusha Banerjee</div></div>
              </div>
            </div>
          </div>

          <!-- 11 to 14 Boys -->
          <div class="category-card">
            <h3 class="category-title">11 TO 14 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sowel Ahmed Gazi</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Avay Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Tanishq Dey</div></div>
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
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Sneha Sinha</div></div>
              </div>
            </div>
          </div>

          <!-- 14 to 17 Boys -->
          <div class="category-card">
            <h3 class="category-title">14 TO 17 BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Probuddha Dutta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Avikho Hazra</div></div>
              </div>
            </div>
          </div>

          <!-- 17 to 21 Female -->
          <div class="category-card">
            <h3 class="category-title">17 TO 21 FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumdar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Dayeta Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Neha Shaw</div></div>
              </div>
            </div>
          </div>

          <!-- 21 to 25 Female -->
          <div class="category-card">
            <h3 class="category-title">21 TO 25 FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sanchaita Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Supriya Panda</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 35 Women -->
          <div class="category-card">
            <h3 class="category-title">25 TO 35 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Rakhi Chatterjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Madhubanti Dey</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Tania Nag</div></div>
              </div>
            </div>
          </div>

          <!-- 25 to 35 Men -->
          <div class="category-card">
            <h3 class="category-title">25 TO 35 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Tapas Paul</div></div>
              </div>
            </div>
          </div>

          <!-- Above 35 Women -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 35 WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sampa Malakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Sonali Ghosh</div></div>
              </div>
            </div>
          </div>

          <!-- Above 35 Men -->
          <div class="category-card">
            <h3 class="category-title">ABOVE 35 MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Manash Mukherjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Pallab Dasgupta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Pijush Kanti Pan</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Single Female (8 - 17 Junior) -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC SINGLE FEMALE (8 - 17 JUNIOR)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Nabomita Dasgupta</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Single Male (8 - 17 Junior) -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC SINGLE MALE (8 - 17 JUNIOR)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sowel Ahmed Gazi</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Single Female (17 - 35 Senior) -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC SINGLE FEMALE (17 - 35 SENIOR)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Tania Nag</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Rakhi Chatterjee</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Pair (8 - 17 Junior) -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC PAIR (8 - 17 JUNIOR)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Rohan Karmakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Sneha Sinha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Payel Saha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Tanisha Das</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Pair Female -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC PAIR FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Rakhi Chaterjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumdar</div></div>
              </div>
            </div>
          </div>

          <!-- Rhythmic (8 - 17 Junior) -->
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC (8 - 17 JUNIOR)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Nabomita Dasgupta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Shubhrajyoti Mahalder</div></div>
              </div>
            </div>
          </div>

          <!-- Rhythmic (17 - 35 Senior) -->
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC (17 - 35 SENIOR)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Rakhi Chaterjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumdar</div></div>
              </div>
            </div>
          </div>

          <!-- Professional Yoga (Female) -->
          <div class="category-card">
            <h3 class="category-title">PROFESSIONAL YOGA (FEMALE)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Chitra Banerjee</div></div>
              </div>
            </div>
          </div>

          <!-- Professional Yoga (Male) -->
          <div class="category-card">
            <h3 class="category-title">PROFESSIONAL YOGA (MALE)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Shiben Mondal</div></div>
              </div>
            </div>
          </div>
"""

with open('results-42nd-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-42nd-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
