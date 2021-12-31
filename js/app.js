const formatCash = n => {
    if (n < 1e3) return n;
    if (n >= 1e3 && n < 1e6) return +(n / 1e3).toFixed(1) + "K";
    if (n >= 1e6 && n < 1e9) return +(n / 1e6).toFixed(1) + "M";
    if (n >= 1e9 && n < 1e12) return +(n / 1e9).toFixed(1) + "B";
    if (n >= 1e12) return +(n / 1e12).toFixed(1) + "T";
  };
  

const load=(coun)=>{

    let imgs=document.querySelector('img');
    let country_name=document.getElementById("state");
    let country_region=document.getElementById("district");
    let country_capital=document.getElementById("market");
    let country_subregion=document.getElementById("commodity");
    let country_alpha3Code=document.getElementById("variety");
    let country_topLevelDomain=document.getElementById("arrival_date");
    let country_demonym=document.getElementById("min_price");
    let country_population=document.getElementById("max_price");
    let country_area=document.getElementById("modal_price");
    
    fetch('https://commodityapi.blob.core.windows.net/commodityapi/db.json', {mode: 'no-cors', method: "get", headers: {"Content-Type": "application/json"}}).then((data)=>{
        return data.json()
    }).then((act)=>{
       
        
        for(var i=0;i<=act.length;i++){
            if(act[i]['name']==coun){
                let state=act[i]['state'];
                let district=act[i]['district'];
                let market=act[i]['market'];
                let commodity=act[i]['commodity'];
                let variety=act[i]['variety'];
                let arrival_date=act[i]['arrival_date'];
                let min_price=act[i]['min_price']
                let max_price=act[i]['max_price'];
                let modal_price=act[i]['modal_price'];

                
                country_borders.innerText="";
                for(let i=0;i<borders.length;i++){
                    country_borders.innerText+=` ${borders[i]}, `;
                }



                imgs.setAttribute("src", national_flag); 
                country_name.innerText=state;
                country_region.innerText=district;
                country_capital.innerText=market;
                country_subregion.innerText=commodity;
                country_alpha3Code.innerText=variety;
                country_topLevelDomain.innerText=arrival_date;
                country_demonym.innerText=min_price;
                country_population.innerText=max_price;
                country_area.innerText=modal_price;
                console.log(act[i])


            }
        }
        
        
    })
}

const getCountry=()=>{
    const coun=document.getElementById('selects').value;
    load(coun)
}