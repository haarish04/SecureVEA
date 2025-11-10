import { useState } from 'react';
import './InputForm.css'

export default function InputForm({ onCheck }) {
  const [phoneNumber, setPhoneNumber] = useState('');

  const handleSubmit = (type) => {
    if (!phoneNumber.trim()) {
      alert('Please enter a phone number');
      return;
    }
    onCheck(type, phoneNumber);
  };

  return (
    <div className="vea-fields">
      <div className="vea-field">
        <span className="vea-label">Mobile Number: </span>
        <input
          type="text"
          className="vea-input"
          value={phoneNumber}
          onChange={(e) => setPhoneNumber(e.target.value)}
        />
      </div>
      <div style={{ display: 'flex', gap: '10px', marginTop: '20px' }}>
        <button className="vea-btn" onClick={() => handleSubmit('sim-swap')}>
          Check SIM Swap
        </button>
        <button className="vea-btn" onClick={() => handleSubmit('device')}>
          Check Device
        </button>
        <button className="vea-btn" onClick={() => handleSubmit('call-forwarding')}>
          Check Call Forwarding
        </button>
      </div>
    </div>
  );
}
