import { useEffect, useMemo, useState } from "react";

 
  // dar bareye [] dar usememo va useeffect:
  // dar moghabele taghirate count usememo triger mishe.na sarfan bar ghararie shart
  // yani vai miste sharte count>10 bar gharar beshe(yani ta ghablesh false boode va hala true shode)
  // hal har cheghad berim jelo taghiri rokh nemide. chon hamchenan true hast va taghiri nakarde.
  // ta count <15 ke ta ghabl az oon false bood va hala taghir mikone va true mishe va
  // dastane usememo: dastan ine ke atar yek usestate dashte bashim. har bar ke estefade beshe baes
  // mishe ke az khate zire const App: React.FC = () => { khoonde beshe ta pain va banabar in tamame chiz mizaro dobare ejra kone
  // pass oon chiziro ke mikhaim mostasna beshe roo too usememo mizarim va vase ejra shodane badish shart
  // tain mikonim. yani agar bekhaim dge ejra nashe [] va age bekhaim tahte sharayeti ejra beshe shart too toosh
  // mizarim masaalan:[count>10,count<15]. dar inja ba har bar zadane dokme yek adad ezafe mishe va kolle chiza dobare
  // anjam mishe va selectedItems ro gozashtim too usememo.
const App: React.FC = () => {
 

  const [count, setCount] = useState(1);
  const [items, setSelectedItems] = useState<string>();

  // useEffect(()=>{console.log('from useeffect')},[count>10,count<15])

  const selectedItems = (): string => {
    //   for (let i = 0; i < new Array(10000).fill(0).length; i++) {
    //  console.log(i)
    // }
    const date = new Date();
    const now =
      date.getHours() + " : " + date.getMinutes() + " : " + date.getSeconds();
    return now;
  };
  // dar inja agar sharte daroone [] bargharar baseh james selectedItems mohasebe mishe
  const james= useMemo(selectedItems,[count>10,count<15])

//  dar inja khastim agar count > 3 shod az oonja be bad har dafe ke dokme count zade mishe, selectedItems ro 
// mohasebe kone. nokte inke dar in ja if dakhele useeffect ghara gerefte va agar useeffect ro dakhele if
// gharar  bedim ifinite loop mishe.
  useEffect(() => {
    if (count > 3) {
      setSelectedItems(() => selectedItems());
    }
  }, [count]);

  return (
    <div>
      <div>{james}</div>
      <div>{items}</div>
      <div>
        <div>{count}</div>
        <button onClick={() => setCount((item) => item + 1)}>eafge</button>
      </div>
    </div>
 
  );
};

export default App;
