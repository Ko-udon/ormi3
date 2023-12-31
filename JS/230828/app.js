// 아래 코드에 관한 모든 권한은 위니브가 가지고 있습니다.
console.log("js가 연결되었습니다");

const data = {
  "id": 1,
  "productName": "버그를 Java라 버그잡는 개리씨 키링 개발자키링 금속키링",
  "price": 12500,
  "stockCount": 100,
  "thumbnailImg": "asset/img/1/thumbnailImg.jpg",
  "option": [],
  "discountRate": 0,
  "shippingFee": 1500,
  "detailInfoImage": [
  "asset/detail/2/detail1.png",
  "asset/detail/2/detail2.png"
  ],
  "viewCount": 0,
  "pubDate": "2022-02-28",
  "modDate": "2022-02-28"
}

const BASE_URL = "보안상 삭제!"
const mainContainer = document.getElementById("main");

//상품 카드 
function createProductCard(imgUrl, price, productName,onClick) {
  const $productCard = document.createElement("div");
  const $productName = document.createElement("strong");
  const $price = document.createElement("span");
  //const $thumbnailImg = document.createElement("img");

  //$thumbnailImg.src = imgUrl;
  $price.innerText = price + "원";
  $productName.innerText = productName;
  //$productCard.append($thumbnailImg, $productName, $price);
  $productCard.append($productName, $price);
  $productCard.addEventListener("click",onClick);

  return $productCard;
}

function createProductDetail(imgUrl) {
    const $productDetail = document.createElement("img");
    $productDetail.src=imgUrl;

    return $productDetail;
}
  


function main() {
  const productsContainer = document.createElement("div");
  productsContainer.id = "products";
  const detailContainer = document.createElement("div");
  detailContainer.id = "detail";
  mainContainer.appendChild(productsContainer);
  mainContainer.appendChild(detailContainer);

  //fetch 하고 난 후 then, res -> respond 패치 하고 난 뒤 결과값을 알려줘 -> 또 그러고 난 후 배열형태의 값을 하나하나 추출해줘
  fetch(BASE_URL+"mall").then((res)=>{
    return res.json();
  }).then((json)=>{
    json.forEach(data=> {
      const productId = data.id;
      const productImgUrl = BASE_URL+data.thumbnailImg;
      const productName = data.productName;
      const price = data.price;
      const onClick = async (e)=>{
        //console.log(productId, "번 상품이 클릭 되었습니다!");
        detailContainer.innerHTML=""  //클릭할때마다 상품 이미지가 계속 생기지 않도록
        //패치를 기다리고 받겠다
        const res = await fetch(BASE_URL+"mall/"+productId);
        const json = await res.json();
        json.detailInfoImage.forEach(imgUrl=>{
          const detailImageUrl = BASE_URL+imgUrl
          const $productDetail = createProductDetail(detailImageUrl);
          detailContainer.appendChild($productDetail);
        })

        //console.log(json);
      }
      const $productCard = createProductCard(productImgUrl,
        price,productName,onClick);

      productsContainer.appendChild($productCard);

    });
  });




  // const productImgUrl = BASE_URL+data.thumbnailImg;
  // const productName = data.productName;
  // const price = data.price;
  // const $productCard = createProductCard(productImgUrl,
  //   price,productName);

  // mainContainer.appendChild($productCard);
}

main();

