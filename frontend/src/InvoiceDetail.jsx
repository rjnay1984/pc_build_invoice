import { useParams } from 'react-router-dom';

function InvoiceDetail() {
  let { invoiceId } = useParams();

  return <div>Invoice id: {invoiceId}</div>;
}

export default InvoiceDetail;
