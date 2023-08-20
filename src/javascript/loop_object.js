/**
 * Code Challenge
 *
 * Map the products from all categories in the `bikes` variable to a variable named `bikeArray`
 * const bikeArray = /* your code here
 */

const bikeObject = {
  road: [
    {
      id: 1,
      modelName: "Ultimate Speed Bike",
      price: 300,
      productImage: "./img/bikes-01.png",
    },
    {
      id: 2,
      modelName: "Road Warrior 2000",
      price: 350,
      productImage: "./img/bikes-02.png",
    },
    {
      id: 3,
      modelName: "Cannonball 23",
      price: 400,
      productImage: "./img/bikes-03.png",
    },
    {
      id: 4,
      modelName: "Storm Chaser",
      price: 450,
      productImage: "./img/bikes-04.png",
    },
  ],
  mountain: [
    {
      id: 5,
      modelName: "Mountain Xplr",
      price: 315,
      productImage: "./img/bikes-05.png",
    },
    {
      id: 6,
      modelName: "Mega Stomper",
      price: 375,
      productImage: "./img/bikes-06.png",
    },
    {
      id: 7,
      modelName: "Yeti SB130 TURQ",
      price: 415,
      productImage: "./img/bikes-07.png",
    },
  ],
  hybrid: [
    {
      id: 8,
      modelName: "City Bike 5",
      price: 340,
      productImage: "./img/bikes-08.png",
    },
    {
      id: 9,
      modelName: "Sunrise",
      price: 340,
      productImage: "./img/bikes-09.png",
    },
    {
      id: 10,
      modelName: "Pegasus",
      price: 340,
      productImage: "./img/bikes-10.png",
    },
  ],
};

function main() {
  let bikeArray = [];

  Object.entries(bikeObject).forEach(([_, productList]) => {
    productList.forEach((product) => {
      bikeArray.push(product);
    });
  });

  console.log(bikeArray);
}

main();
