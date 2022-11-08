import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [state, setState] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const { data } = await axios.get("/api");
      setState(data);
    }
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <div>{`DATA is here ${state}`}</div>
        <p>
          Fitness Tracker
        </p>
      </header>
    </div>
  );
}

export default App;
