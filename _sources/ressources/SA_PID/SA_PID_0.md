<div style="background-color: #fff3cd; border: 2px solid #ffc107; border-radius: 5px; padding: 8px 12px; margin: 15px 0; text-align: center;">
  <strong style="color: #856404; font-size: 14px;">⚠️ VERSION DE TRAVAIL</strong>
  <span style="color: #856404; margin-left: 10px; font-size: 13px;">
    Document en cours de développement à ne pas diffuser tel quel.
  </span>
</div>

<div style="background-color: #e8f5e9; padding: 8px 12px; margin: 15px 0; border-radius: 5px; text-align: center; font-size: 14px;">
  💬 <strong>Améliorons ensemble la proposition !</strong> Surlignez du texte et cliquez sur "Annotate"
</div>


# SA PID
objectifs généraux du sujet : dans ces fiches autour des correcteurs, tu pourras donner du sens au formalisme graphique des correcteurs (schémas blocs), mais aussi aux coefficients P, I et D. 
Tu verras aussi des points d'attention associés aux comportements des capteurs, et on donnera du sens physique aux notions de temps de réponse et erreur statique par exemple.  



<div class="card-container">


  <!-- Carte 1 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
    pid.1 : notion de correcteur
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive1.png" alt="correcteur" class="img-responsive">
      <p> comprendre le role de chaque élément dans un schéma bloc. Découvrir le formalisme graphique si tu ne l'as jamais vu </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_1.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 2 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.2 : boucles et schémas blocs
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive2.png" alt="boucles" class="img-responsive">
      <p> distinguer les boucles de correction dans un schéma bloc un peu complexe  </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_2.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  
  <!-- Carte 3 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.3 : PID correction proportionnelle
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive3.png" alt="proportionnel" class="img-responsive">
      <p> comprendre l'influence du coefficient P ou Kp. Comprendre son rôle sur la vitesse de la réponse et les raisons qui font qu'il crée des oscillations </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_3.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 4 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.4 : influence de m et k 
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive4.png" alt="k_et_m" class="img-responsive">
      <p> se convaincre physiquement de l'influence de k et m sur la fréquence d'oscillation, ne plus se tromper sur le sens de l'écriture de la pulsation </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_4.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 5 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.5 : correction dérivée
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive5.png" alt="derivee" class="img-responsive">
      <p> comprendre le role du coefficient D ou Kd. Comprendre que la forme de la réponse amortie globale est liée à la fois à Kd mais aussi à sa valeur par rapport à Kp et m </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_5.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 6 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.6 : temps de réponse 
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive6.png" alt="temps_rep" class="img-responsive">
      <p> comprendre le critère de temps de réponse et l'analyser pour des systèmes très amortis ou oscillants </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_6.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 7 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.7 : causalité
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive7.png" alt="causalite" class="img-responsive">
      <p> comprendre les limites physiques (la vraie vie) d'un modèle analytique qui s'appuie sur v(t). Comprendre aussi pourquoi dans une fonction de transfert le polynome du dénominateur est toujours d'ordre plus grand que le numérateur </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_7.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 8 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.8 : capteurs
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive8.png" alt="capteur" class="img-responsive">
      <p> comprendre les risques associés aux capteurs réels et la nécessité de filtrages des signaux avant l'entrée dans le bloc de correction </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_8.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 9 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.9 : equation amortie
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive9.png" alt="ksi" class="img-responsive">
      <p> rappeler la définition de l'amortissement analytique ski et le comportement de part et d'autre de ses seuils (1 et 0,7) </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_9.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 10 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.10 : erreur statique 
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive10.png" alt="err_stat" class="img-responsive">
      <p> comprendre pourquoi sans correction integral il reste souvent une erreur statique et la logique physique du signe de cette erreur résiduelle </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_10.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 11 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.11 : correction intégrale
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive11.png" alt="integral" class="img-responsive">
      <p> Comprendre le rôle du coefficient I ou Ki. Comprendre les risques de destabilisation associés à un I trop grand </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_11.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>

  <!-- Carte 12 -->
  <div class="card">
    <div class="card-header" style="text-align: center;">
      pid.12 : une conclusion sur les PID
    </div>
    <div class="card-body">
      <img src="../../_static/images/SA/PID/PID_Diapositive12.png" alt="yoda" class="img-responsive">
      <p> une conclusion </p>
      <p class="card-footer-link">
        <a href="../SA_PID/SA_PID_12.html" class="card-link">
          Voir la fiche <i class="fas fa-arrow-right"></i>
        </a>
      </p>
    </div>
  </div>


</div>



<br>
<br>

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 30px; position: relative;">
  <a href="../SA__index.html" style="display: inline-block; padding: 6px 30px; background-color: #bec9dcff; color: white; text-decoration: none; border-radius: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s; text-align: center; position: absolute; left: 50%; transform: translateX(-50%);">
    🔄 Retour aux thématiques <br> 'systèmes asservis'
  </a>
</div>

<br>
<br>

## Le pdf du sujet complet dans sa version livre (2 pages cote à cote)
*Version de travail , ne pas diffuser tel quel, merci à vous.* 


<iframe 
  src="../../_static/pdfs/PIDv4_v2.pdf#toolbar=0&navpanes=0&scrollbar=0" 
  style="width:100%; height:600px;"
  title="Document PDF">
</iframe>


<br>

<br>
<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 30px; position: relative;">
  <span style="color: #333; font-weight: normal;">Sujet</span>
  <a href="../SA__index.html" style="display: inline-block; padding: 6px 30px; background-color: #bec9dcff; color: white; text-decoration: none; border-radius: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s; text-align: center; position: absolute; left: 50%; transform: translateX(-50%);">
    🔄 Retour aux thématiques <br> 'systèmes asservis'
  </a>
  <span style="margin-left: auto; color: #333; font-weight: normal;">Sujet</span>
</div>