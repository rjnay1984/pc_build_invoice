import { Link } from 'react-router-dom'
import './App.css';

function App() {
  return (
    <div className="App">
      <header>
        <nav>
          <span className="navbar-brand">Pc Build Invoice</span>
          <ul>
            <li><Link to="/invoices">Invoices</Link></li>
          </ul>
        </nav>
      </header>
    </div>
  );
}

export default App;
