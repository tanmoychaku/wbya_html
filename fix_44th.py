import re

HTML = """
          <!-- Sub Junior Group A (Boys 8-10 Years) -->
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP A (BOYS 8-10 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">SUPRIYO SARKAR</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">SHIBAM DEBNATH</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">SWATTIK KOLE</div></div>
              </div>
            </div>
          </div>

          <!-- Sub Junior Group A (Girls 8-10 Years) -->
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP A (GIRLS 8-10 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">POUSALI KANGSABANIK</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">PRITHA KARMAKAR</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">SAYANTITA MUKHERJEE</div></div>
              </div>
            </div>
          </div>

          <!-- Sub Junior Group B (Boys 10-12 Years) -->
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP B (BOYS 10-12 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">SUBHAMAY ROY</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">RITAM DAS</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">RUPANKAR DATTA</div></div>
              </div>
            </div>
          </div>

          <!-- Sub Junior Group B (Girls 10-12 Years) -->
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP B (GIRLS 10-12 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">SAMPRITA SAHA</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">SRIJA SAHA</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">SHREYA CHOWDHURY</div></div>
              </div>
            </div>
          </div>

          <!-- Sub Junior Group C (Boys 12-14 Years) -->
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP C (BOYS 12-14 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">SUSMIT BISWAS</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">MANASH KARMAKAR</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">SOUMIK PAN</div></div>
              </div>
            </div>
          </div>

          <!-- Sub Junior Group C (Girls 12-14 Years) -->
          <div class="category-card">
            <h3 class="category-title">SUB JUNIOR GROUP C (GIRLS 12-14 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">PAYEL SAHA</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">KAUSHANI TALUKDAR</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">PRATYUSHA BANERJEE</div></div>
              </div>
            </div>
          </div>

          <!-- Junior Group A (Boys 14-16 Years) -->
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP A (BOYS 14-16 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">KOUSHIK BAIRAGI</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">JYOTISHKA BAIN</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">SOWEL AHMED GAZI</div></div>
              </div>
            </div>
          </div>

          <!-- Junior Group A (Girls 14-16 Years) -->
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP A (GIRLS 14-16 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">RITU MONDAL</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">OLIVA BHATTACHARYYA</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-6">6th</div>
                <div class="winner-info"><div class="winner-name">ABANTIKA BISWAS</div></div>
              </div>
            </div>
          </div>

          <!-- Junior Group B (Boys 16-18 Years) -->
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP B (BOYS 16-18 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">ARPAN BOSE</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">PRASUN BISWAS</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">RATUL SAHA</div></div>
              </div>
            </div>
          </div>

          <!-- Junior Group B (Girls 16-18 Years) -->
          <div class="category-card">
            <h3 class="category-title">JUNIOR GROUP B (GIRLS 16-18 YEARS)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">RAJANYA DAS</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">SAKSHI DUTTA</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">SHUBHAMITA CHATTERJEE</div></div>
              </div>
            </div>
          </div>

          <!-- Professional Yogasana Competition (Women above 30 Years) -->
          <div class="category-card">
            <h3 class="category-title">PROFESSIONAL YOGASANA (WOMEN ABOVE 30)</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">ANNESWA SINHA</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">CHITRA BANERJEE</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-4">4th</div>
                <div class="winner-info"><div class="winner-name">MANASI MANNA HALDAR</div></div>
              </div>
            </div>
          </div>
"""

with open('results-44th-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-44th-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
