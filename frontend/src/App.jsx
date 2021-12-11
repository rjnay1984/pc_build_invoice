import './App.css';

import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Navbar from './components/Navbar';
import Home from './Home';
import InvoiceDetail from './InvoiceDetail';
import InvoiceList from './InvoiceList';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <header>
          <Navbar />
        </header>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/invoices" element={<InvoiceList />} />
          <Route path="/invoices/:invoiceId" element={<InvoiceDetail />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
