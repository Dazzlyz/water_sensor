import './App.css';

function App() {
  let name = 'Menno';
  let date = 28;
  const link = 'https://wiki.seeedstudio.com/Grove-Moisture_Sensor/'; 
  return (
    <div className="App">
      <div className='content'></div>
        <h1>{name}'s Component</h1>
        <p>created {date} febraury</p>
        <a href={link}> Product used</a>
    </div>
  );
}

export default App;
