// src/components/PaymentPage.js

import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { FlutterWaveButton, closePaymentModal } from 'flutterwave-react-v3';
import './PaymentPage.css';
import Header from '../utils/header/Header';
import Footer from '../utils/footer/Footer';

const PaymentPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { state } = location;
  
  const { totalAmount, customerDetails, movieTitle, cinemaName, showtime, movieImage} = state;

  const config = {
    public_key: 'FLWPUBK_TEST-e2774ae793c9a638c2d8491337c21f15-X',
    tx_ref: Date.now(),
    amount: totalAmount,
    currency: 'KES',
    payment_options: 'card,mpesa',
    customer: {
      email: customerDetails.email,
      
    },
    customizations: {
      title: `${movieTitle} Ticket Purchase`,
      description: `Payment for movie ticket at ${cinemaName}, Showtime: ${showtime}`,
      logo: movieImage,
    },
  };

  const handleFlutterwavePayment = (response) => {
    closePaymentModal(); // this will close the modal programmatically
    // handle any post-payment actions here

    // Navigate to the receipt page with the transaction details
    navigate(`/receipt/${response.transaction_id}`, { state: { ...response, movieTitle, cinemaName, showtime, movieImage, totalAmount } });
  };

  return (
    <div className="payment-page">
      <Header />
      <div className='dets'>
        <h1 style={{color: '#FFE1E9'}}>Payment for {movieTitle}</h1>
        <img src={movieImage} alt='movie' style={{width: '400px', height: 'auto', borderRadius: '8px'}}/>
        <div className='details'>
        <p style={{color: '#FFE1E9'}}>Cinema: {cinemaName}</p>
        <p style={{color: '#FFE1E9'}}>Showtime: {showtime}</p>
        <p style={{color: '#FFE1E9'}}>Total Amount: KES{totalAmount}</p>
        </div>
        
        <FlutterWaveButton
          callback={handleFlutterwavePayment}
          onClose={() => {}}
          {...config}
          className='button'
          text="Proceed to Payment"
        />
      </div>
      <Footer />
    </div>
  );
};

export default PaymentPage;
