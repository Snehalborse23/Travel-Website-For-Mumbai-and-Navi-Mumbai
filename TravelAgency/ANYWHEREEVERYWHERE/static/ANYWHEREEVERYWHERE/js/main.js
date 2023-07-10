const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function submitRating(location) {
    event.preventDefault();
    const rating = document.getElementById(location + "-rating").value;
    console.log("location:", location, "rating:", rating);
  
fetch(`/save_rating/${location}/${rating}`)
    .then(response => response.json())
    .then(data => {
        console.log("data:", data);
      document.getElementById(location + "-rating-msg").textContent = "Thanks for rating!";
      document.getElementById(location + "-avg-rating").textContent = "Average rating: " + data.avg_rating;
      const avgRatingDiv = document.getElementById("avg-rating");
      avgRatingDiv.textContent = "Average rating: " + data.avg_rating.toFixed(1);
    })
  }
  
  function submitReview(location, review, rating) {
    console.log(location, review, rating);
    fetch(`/save_review/${location}/${review}/${rating}`)
      .then(response => response.json())
      .then(data => {
        console.log("data:", data);
      });

    clear()
  }

  function clear(){
    console.log("cleared Called")
    document.getElementById('rockGarden').value="";
    document.getElementById('rating_rockGarden').value ="";

    console.log("cleared Called")
    document.getElementById('jewel-of-navi-mumbai').value="";
    document.getElementById('jewels_rating').value ="";

    console.log("cleared Called")
    document.getElementById('PrashantCorner').value="";
    document.getElementById('rating_PrashantCorner').value ="";

    console.log("cleared Called")
    document.getElementById('BarbequeNation').value="";
    document.getElementById('rating_BarbequeNation').value ="";

    document.getElementById('ParsikHill').value="";
    document.getElementById('rating_ParsikHill').value ="";

    document.getElementById('BelapurFort').value="";
    document.getElementById('rating_BelapurFort').value ="";

    document.getElementById('ChaiSuttaBar').value="";
    document.getElementById('rating_ChaiSuttaBar').value ="";

    document.getElementById('Chanakya').value="";
    document.getElementById('rating_Chanakya').value ="";

    document.getElementById('T-SpawnGamersCafe').value="";
    document.getElementById('rating_T-SpawnGamersCafe').value ="";

    document.getElementById('DYPatilStadium').value="";
    document.getElementById('rating_DYPatilStadium').value ="";

    document.getElementById('PirwadBeach').value="";
    document.getElementById('rating_PirwadBeach').value ="";

    document.getElementById('ShamiyanaRestaurant').value="";
    document.getElementById('rating_ShamiyanaRestaurant').value ="";

    document.getElementById('VaishnaviRestaurant').value="";
    document.getElementById('rating_VaishnaviRestaurant').value ="";

    document.getElementById('DronagiriFort').value="";
    document.getElementById('rating_DronagiriFort').value ="";

    document.getElementById('BunkerzzCafe').value="";
    document.getElementById('rating_BunkerzzCafe').value ="";


    document.getElementById('VimlaTalao').value="";
    document.getElementById('rating_VimlaTalao').value ="";

    document.getElementById('IskconTemple').value="";
    document.getElementById('rating_IskconTemple').value ="";


    document.getElementById('LittleWorldMall').value="";
    document.getElementById('rating_LittleWorldMall').value ="";

    document.getElementById('PandavkadaWaterfalls').value="";
    document.getElementById('rating_PandavkadaWaterfalls').value ="";

    document.getElementById('CentralPark').value="";
    document.getElementById('rating_CentralPark').value ="";

    document.getElementById('KhargharHills').value="";
    document.getElementById('rating_KhargharHills').value ="";

    document.getElementById('UtsavChowk').value="";
    document.getElementById('rating_UtsavChowk').value ="";

    document.getElementById('ValleyGolfCourse').value="";
    document.getElementById('rating_ValleyGolfCourse').value ="";

    document.getElementById('MiniSeashore').value="";
    document.getElementById('rating_MiniSeashore').value ="";

    document.getElementById('NavaratnaRestaurant').value="";
    document.getElementById('rating_NavaratnaRestaurant').value ="";

    document.getElementById('SagarVihar').value="";
    document.getElementById('rating_SagarVihar').value ="";

    document.getElementById('InorbitMall').value="";
    document.getElementById('rating_InorbitMall').value ="";

    document.getElementById('RaghuleelaMall').value="";
    document.getElementById('rating_RaghuleelaMall').value ="";

    document.getElementById('band').value="";
    document.getElementById('rating_band').value ="";

    document.getElementById('fort').value="";
    document.getElementById('rating_fort').value ="";

    document.getElementById('church').value="";
    document.getElementById('rating_church').value ="";


    document.getElementById('candies').value="";
    document.getElementById('rating_candies').value ="";


    document.getElementById('jpark').value="";
    document.getElementById('rating_jpark').value ="";
             document.getElementById('tajtea').value="";
    document.getElementById('rating_tajtea').value ="";

    document.getElementById('pmall').value="";
    document.getElementById('rating_pmall').value ="";

    document.getElementById('gate').value="";
    document.getElementById('rating_gate').value ="";

    document.getElementById('taj').value="";
    document.getElementById('rating_taj').value ="";

    document.getElementById('cc').value="";
    document.getElementById('rating_cc').value ="";

    document.getElementById('marine').value="";
    document.getElementById('rating_marine').value ="";

    document.getElementById('isckon').value="";
    document.getElementById('rating_isckon').value ="";


    document.getElementById('cpatty').value="";
    document.getElementById('rating_cpatty').value ="";


    document.getElementById('stadium').value="";
    document.getElementById('rating_stadium').value ="";

    document.getElementById('tp').value="";
    document.getElementById('rating_tp').value ="";


    document.getElementById('temple').value="";
    document.getElementById('rating_temple').value ="";


    document.getElementById('lcafe').value="";
    document.getElementById('rating_lcafe').value ="";

    document.getElementById('mcafe').value="";
    document.getElementById('rating_mcafe').value ="";

    document.getElementById('ecaves').value="";
    document.getElementById('rating_ecaves').value ="";

    document.getElementById('mabeach').value="";
    document.getElementById('rating_mabeach').value ="";

    document.getElementById('bounce').value="";
    document.getElementById('rating_bounce').value ="";


    document.getElementById('mimall').value="";
    document.getElementById('rating_mimall').value ="";
    document.getElementById('aiskcon').value="";
    document.getElementById('rating_aiskcon').value ="";

    document.getElementById('amcaves').value="";
    document.getElementById('rating_amcaves').value ="";

    document.getElementById('rcity').value="";
    document.getElementById('rating_rcity').value ="";

    document.getElementById('versovapvr').value="";
    document.getElementById('rating_versovapvr').value ="";


    document.getElementById('aarey').value="";
    document.getElementById('rating_aarey').value ="";


    document.getElementById('PhoenixMall').value="";
    document.getElementById('rating_PhoenixMall').value ="";


    document.getElementById('sktemple').value="";
    document.getElementById('rating_sktemple').value ="";

    document.getElementById('rmahal').value="";
    document.getElementById('rating_rmahal').value ="";

    document.getElementById('naaz').value="";
    document.getElementById('rating_naaz').value ="";

    document.getElementById('spark').value="";
    document.getElementById('rating_spark').value ="";

  }
