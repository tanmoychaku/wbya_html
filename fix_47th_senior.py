import os

HTML = """
          <!-- Senior Group A Female -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-A (18-21 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sakshi Dutta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Taniya Dutta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sudeshna Golder</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group A Male -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-A (18-21 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Avay Sarkar</div></div>
              </div>
            </div>
          </div>
          
          <!-- Senior Group B Female -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-B (21-25 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sneha Sinha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumder</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sanchita Kar</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group B Male -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-B (21-25 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sourya Bagchi</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Saibal Guchait</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group C Female -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-C (25-30 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sanchaita Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Suchitra Debnath</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Supriya Panda</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group C Male -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-C (25-30 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sanat Pakhira</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Binay Ranjan</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group D Female -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-D (30-35 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Pallabi Ghar Sen</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank">4th</div>
                <div class="winner-info"><div class="winner-name">Dolon Manna</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank">5th</div>
                <div class="winner-info"><div class="winner-name">Mili Sarkar</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group D Male -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-D (30-35 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Shyam Sundar Golder</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Mohan Kr. Singh</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group E Female -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-E (35-45 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Shampa Malakar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Tina Khatun</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Shrabani Sett</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group E Male -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-E (35-45 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Laxmi Kanta Adak</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank">5th</div>
                <div class="winner-info"><div class="winner-name">Shyamal Banerjee</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group F Female -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-F (Above 45 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Debjani Biswas</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank">4th</div>
                <div class="winner-info"><div class="winner-name">Amita Majumder</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group F Male -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP-F (Above 45 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Pijush Kanti Pan</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Partha Ghosh</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank">5th</div>
                <div class="winner-info"><div class="winner-name">Pallab Dasgupta</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Artistic Single Female -->
          <div class="category-card">
            <h3 class="category-title">SENIOR ARTISTIC SINGLE - FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumder</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Artistic Single Male -->
          <div class="category-card">
            <h3 class="category-title">SENIOR ARTISTIC SINGLE - MALE</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Avay Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank">6th</div>
                <div class="winner-info"><div class="winner-name">Sourya Bagchi</div></div>
              </div>
            </div>
          </div>

          <!-- Rhythmic Female -->
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC (FEMALE)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumder &amp; Sneha Sinha</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Pair Male -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC PAIR (MALE)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sayan Roy &amp; Ratul Saha</div></div>
              </div>
            </div>
          </div>

          <!-- Rhythmic Male -->
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC (MALE)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sayan Roy &amp; Saibal Guchait</div></div>
              </div>
            </div>
          </div>
"""

with open('results-47th-senior-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Replace the category-grid contents with our hardcoded perfect HTML
new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-47th-senior-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
