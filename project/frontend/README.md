# Front End
## Che cos'è?

Front end è classico, lo sappiamo già fare con HTML, CSS, JS.

## Alcune Linee Guida

Per agevolare la collaborazione, abbiamo scelto alcune linee guida che sarebbe meglio seguire

### Html, CSS
Cercate di mettere i commenti, sopratutto se non si capisce a vista d'occhio cosa una tag o una classe CSS fanno

### Javascript
* I punti e virgola sono opzionali, ma cercate di metterli sempre.
* Mettete sempre un numero adeguato di commenti.
* *Cercate* di mantenere le funzioni corte ed autoesplicative, così che tutto sia più ordinato.
  * se proprio la funzione viene lunga, commentatela in modo che sia chiaro come sia divisa. Ad esempio: 
```javascript
/*TITOLO DI SEZIONE*/
function myFunction(a,b){
  /*TITOLO DI SEZIONE*/
  let x = 0;
  x += myFunc2(x+13);
  //titolo sottosezione
  let y = myFunc3(15,x);
  y += myFunc4(x,y);
  /*TITOLO DI SEZIONE*/
  let z = (x+y)/2;
  while (myFunc6(x,y,z)!=0){
  //titolo sezione
  console.log("ciao");
  z += x+y*2;//commento corto
  }
  return z;
}
```