import re
import shutil

# 1. 44th Senior
html_44th_senior = """
          <!-- Senior Group A Boys (18 to 21) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'A' BOYS (18 TO 21)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Sourya Bagchi</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Pronoy Mondal</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group A Girls (18 to 21) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'A' GIRLS (18 TO 21)</h3>
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
                <div class="winner-info"><div class="winner-name">Dayeta Sarkar</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group B Men (21 to 25) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'B' MEN (21 TO 25)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Vivekananda Pal</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Ganesh Pal</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group B Women (21 to 25) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'B' WOMEN (21 TO 25)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Neha Shaw</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group C Men (25 to 30) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'C' MEN (25 TO 30)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Deepak Gond</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Mohan Kumar singh</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Shyam Sundar Goldar</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group C Women (25 to 30) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'C' WOMEN (25 TO 30)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sanchaita Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Pallabi Ghar (Sen)</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Madhubanti Dey</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group D Men (30 to 35) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'D' MEN (30 TO 35)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Shibnath Basak</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Brajanath Basak</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group D Women (30 to 35) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'D' WOMEN (30 TO 35)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Nupur Debnath</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Dolon Manna</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Alpana Sarkar (Ghosh)</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group E Men (35 to 45) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'E' MEN (35 TO 45)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Laxmikanta Adak</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group E Women (35 to 45) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'E' WOMEN (35 TO 45)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Sonali Ghosh (Dutta)</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Asha Sarkar</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group F Men (Above 45) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'F' MEN (ABOVE 45)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Manash Mukherjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Pallab Dasgupta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Pijush Kanti Pan</div></div>
              </div>
            </div>
          </div>

          <!-- Senior Group F Women (Above 45) -->
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP 'F' WOMEN (ABOVE 45)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Debjani Biswas Mondal</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Mithu Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Amita Majumder</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Yoga Senior (18 to 35) Single Boys -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC YOGA SENIOR SINGLE BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Vivekananda Pal</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">Pronoy Mondal</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Yoga Senior (18 to 35) Single Girls -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC YOGA SENIOR SINGLE GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumder</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Dayeta Sarkar</div></div>
              </div>
            </div>
          </div>

          <!-- Artistic Yoga Senior (18 to 35) Pair -->
          <div class="category-card">
            <h3 class="category-title">ARTISTIC YOGA SENIOR PAIR</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumder</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sneha Sinha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Dayeta Sarkar</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">Neha Shaw</div></div>
              </div>
            </div>
          </div>

          <!-- Rhythmic Yoga Senior (18 to 35) -->
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC YOGA SENIOR</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumder</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Sneha Sinha</div></div>
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

          <!-- Free Flow Yoga -->
          <div class="category-card">
            <h3 class="category-title">FREE FLOW YOGA</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-5">5th</div>
                <div class="winner-info"><div class="winner-name">Anusha Majumder, Dayeta Sarkar, Sneha Sinha, Vivekananda Pal, Pronoy Mondal</div></div>
              </div>
            </div>
          </div>
"""
shutil.copy('base.html', 'results-44th-senior-national-yoga-championship-2019.html')
with open('results-44th-senior-national-yoga-championship-2019.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('{{CHAMPIONSHIP_TITLE}}', '44th Senior National Yoga Championship, 2019')
content = content.replace('{{CHAMPIONSHIP_VENUE}}', 'Jaipur (Rajasthan)')
content = content.replace('{{CHAMPIONSHIP_DATE}}', 'November 9-12, 2019')
content = content.replace('{{CHAMPIONSHIP_WINNER}}', 'West Bengal (75.0)')
content = content.replace('{{CHAMPIONSHIP_RUNNER_UP}}', 'Rajasthan (35.0)')
content = content.replace('{{CHAMPIONSHIP_SECOND_RUNNER_UP}}', 'Maharashtra (28.0)')
content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{html_44th_senior}</div></div></section>', content, flags=re.DOTALL)

with open('results-44th-senior-national-yoga-championship-2019.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. 45th Edition
html_45th = """
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP A (8-10 YEARS) BOYS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Deepanshu Sinha</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Supriyo Sarkar</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Debashis Das</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP A (8-10 YEARS) GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Nitisha Patra</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Pousali Kangsabanik</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Debopriya Chatterjee</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP B (10-12 YEARS, BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Samrat Sen</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Ritam Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Shibam Debnath</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP B (10-12 YEARS, GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Srija Saha</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Adrija Biswas</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Pyushpita Debnath</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP C (12-14 YEARS BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Manash Karmakar</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Soumik Pan</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Sougata Paul</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP C (12-14 YEARS GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Tanisha Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Payel Saha</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Jhuma Dey</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP A (14-16 YEARS, BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Jyotishka Bain</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Koushik Bairagi</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-6">6th</div><div class="winner-info"><div class="winner-name">Sowel Ahmed Gazi</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP A (14-16 YEARS, GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Abantika Biswas</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Ritu Mondal</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Rupsa Dutta</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP B (16 -18 YEARS BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Arpan Bose</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Sayan Roy</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Pijush Pal</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP B (16 -18 YEARS GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Sudeshna Golder</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Oliva Bhattacharyya</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Shubhamita Chatterjee</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP A (18-21 YEARS BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Saibal Guchait</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Sourya Bagchi</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Pronoy Mondal</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP A (18-21 YEARS GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Sakshi Dutta</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Anusha Majumder</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Nabomita Dasgupta</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP B (21-25 YEARS BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Vivekananda Pal</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-6">6th</div><div class="winner-info"><div class="winner-name">Swapnanil Kayal</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP B (21-25 YEARS GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Dayeta Sarkar</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Neha Shaw</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP C (BOYS 25-30)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Shyam Sundar Golder</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP C (GIRLS 25-30)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Sarmistha Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Pallabi Ghar (Sen)</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Suchitra Debnath</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP D (BOYS 30-35)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Sambhuram Bar</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP D (GIRLS 30-35)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Indrani Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Dolon Manna</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Tina Khatun</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP E (BOYS 35-45)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Laxmi Kanta Adak</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP E (GIRLS 35-45)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Shrabani Sett</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Shampa Malakar (Das)</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Sonali Ghosh</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP F (BOYS ABOVE 45)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">PALLAB DASGUPTA</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">PARTHA GHOSH</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">PIJUSH KANTI PAN</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP F (GIRLS ABOVE 45)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Debjani Biswas Mondal</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR ARTISTIC SOLO MALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Ritam Das</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR ARTISTIC SOLO FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Ritu Mondal</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Jhuma Dey</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR ARTISTIC SOLO FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Nabamita Dasgupta</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">FEMALE PROFESSIONAL GROUP ABOVE 30</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Chitra Banerjee</div></div></div>
            </div>
          </div>
"""

with open('results-45th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{html_45th}</div></div></section>', content, flags=re.DOTALL)
with open('results-45th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 3. 46th SJ&J
html_46th = """
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP A (8-10 YEARS) BOYS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Deepanshu Sinha</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Saikat Ghosh</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Prem Thaner</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP A (8-10 YEARS) GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Nitisha Patra</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Sampriti Chatterjee</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Swastika Pal</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP B (10-12 YEARS, BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Swattik Koley</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Supriyo Sarkar</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-5">5th</div><div class="winner-info"><div class="winner-name">Shibam Debnath</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP B (10-12 YEARS, GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Poushali Kangsabanik</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Shrestha Rana</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Pritha Karmakar</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP C (12-14 YEARS BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-5">5th</div><div class="winner-info"><div class="winner-name">Ritam Das</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP C (12-14 YEARS GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-5">5th</div><div class="winner-info"><div class="winner-name">Sampriti Saha</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-6">6th</div><div class="winner-info"><div class="winner-name">Aditi Yadav</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP A (14-16 YEARS, BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Soumik Pan</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Bipratip Banerjee</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-5">5th</div><div class="winner-info"><div class="winner-name">Ajoy Soren</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP A (14-16 YEARS, GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Payel Saha</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Tanisha Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Jhuma Dey</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP B (16-18 YEARS BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Koushik Bairagi</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Jyotishka Bain</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Avay Sarkar</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP B (16-18 YEARS GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Ritu Mondal</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Sudeshna Golder</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Swarnali Ghosh</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">ARTISTIC SOLO MALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Ritam Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Koushik Bairagi</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">ARTISTIC SOLO FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-6">6th</div><div class="winner-info"><div class="winner-name">Ritu Mondal</div></div></div>
            </div>
          </div>
"""
with open('results-46th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{html_46th}</div></div></section>', content, flags=re.DOTALL)
with open('results-46th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 4. 46th Senior
html_46th_senior = """
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP A (18-21 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">SAKSHI DUTTA</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">SANCHITA KAR</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">SNEHA SINHA</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP A (18-21 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">SAIBAL GUCHAIT</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">SOURYA BAGCHI</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">PIYUSH PAL</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP B (21-25 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">ANUSHA MAJUMDER</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">DAYETA SARKAR</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">SANCHITA DEBNATH</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP B (21-25 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-6">6th</div><div class="winner-info"><div class="winner-name">VIVEKANANDA PAL</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-6">6th</div><div class="winner-info"><div class="winner-name">LOKNATH DAS</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP C (25-30 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">SANCHAITA CHAKRABORTY</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">SARMISTHA DAS</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">SUCHITRA DEBNATH</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP C (25-30 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">JOSIMUDDIN MOLLA</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-6">6th</div><div class="winner-info"><div class="winner-name">SHYAMSUNDAR GOLDAR</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP D (30-35 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">TINA KHATUN</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">DOLON MANNA</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">MILI SARKAR</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP D (30-35 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">BISWAJIT PAUL</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">SAMBHURAM BAR</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-5">5th</div><div class="winner-info"><div class="winner-name">ASHIS MAJUMDER</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP E (35-45 YEARS) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">SHAMPA MALAKAR DAS</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">SHRABANI SETT</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP E (35-45 YEARS) MALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">LAXMI KANTA ADAK</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-5">5th</div><div class="winner-info"><div class="winner-name">SHYAMAL BANERJEE</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP F (ABOVE 45) FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">MOUSUMI MANNA</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">DEBJANI BISWAS MONDAL</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">AMITA MAJUMDER</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR GROUP F (ABOVE 45) MALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">PIJUSH KANTI PAN</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">PALLAB DASGUPTA</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">PARTHA GHOSH</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR ARTISTIC SINGLE FEMALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">ANUSHA MAJUMDER</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">DAYETA SARKAR</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SENIOR ARTISTIC SINGLE MALE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">SOURYA BAGCHI</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-6">6th</div><div class="winner-info"><div class="winner-name">PIYUSH PAL</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">ARTISTIC PAIR (FEMALE)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">ANUSHA MAJUMDER</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">SNEHA SINHA</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC PAIR (FEMALE)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">SNEHA SINHA</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">DAYETA SARKAR</div></div></div>
            </div>
          </div>
"""
with open('results-46th-senior-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{html_46th_senior}</div></div></section>', content, flags=re.DOTALL)
with open('results-46th-senior-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 5. 47th SJ&J
html_47th = """
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP A (8-10 YEARS) BOYS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Sayan Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Priyangshu Bag</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Abhinayu Barman</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP A (8-10 YEARS) GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Samriddhi Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Poushani Saha</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Oishiki Mukherjee</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP B (10-12 YEARS, BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Dyutimoy Jana</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Supriyo Sarkar</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Saikat Ghosh</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP B (10-12 YEARS, GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Rankita Mondal</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Poushali Kangsabanik</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Swastika Pal</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP C (12-14 YEARS BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Ritam Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Swattik Koley</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Samrat Sen</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP C (12-14 YEARS GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Oindreela Bor</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Srija Saha</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Puspita Debnath</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP A (14-16 YEARS, BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Soumik Pan</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Ayush Chatterjee</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP A (14-16 YEARS, GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Tanisha Das</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-5">5th</div><div class="winner-info"><div class="winner-name">Payel Talukder</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP B (16-18 YEARS BOYS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Koushik Bairagi</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Ajoy Soren</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Binod Chowdhury</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP B (16-18 YEARS GIRLS)</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Ritu Mondal</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-3">3rd</div><div class="winner-info"><div class="winner-name">Koyel Tanti</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Swarnali Ghosh</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">ARTISTIC SOLO BOYS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-4">4th</div><div class="winner-info"><div class="winner-name">Koushik Bairagi</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">ARTISTIC SOLO GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Ritu Mondal</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Srija Saha</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">ARTISTIC PAIR BOYS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Soumik Pan</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Saikat Ghosh</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">ARTISTIC PAIR GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-5">5th</div><div class="winner-info"><div class="winner-name">Swarnali Ghosh</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-5">5th</div><div class="winner-info"><div class="winner-name">Payel Talukder</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC BOYS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Supriyo Sarkar</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Ritam Das</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">RHYTHMIC GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Srija Saha</div></div></div>
              <div class="winner-item"><div class="winner-rank rank-2">2nd</div><div class="winner-info"><div class="winner-name">Rankita Mondal</div></div></div>
            </div>
          </div>
          <div class="category-card">
            <h3 class="category-title">FREE FLOW YOGA DANCE</h3>
            <div class="winners-list">
              <div class="winner-item"><div class="winner-rank rank-1">1st</div><div class="winner-info"><div class="winner-name">Koushik Bairagi, Payel Talukder, Rankita Mondal, Swarnali Ghosh, Srija Saha</div></div></div>
            </div>
          </div>
"""
with open('results-47th-sub-junior-junior-national-yogasana-sports-championship-2022.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{html_47th}</div></div></section>', content, flags=re.DOTALL)
with open('results-47th-sub-junior-junior-national-yogasana-sports-championship-2022.html', 'w', encoding='utf-8') as f:
    f.write(content)
