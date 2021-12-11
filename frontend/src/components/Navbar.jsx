import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <span className="navbar-brand">Pc Build Invoice</span>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/invoices">Invoices</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
