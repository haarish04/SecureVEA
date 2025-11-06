import { useState } from 'react';
import InputForm from './components/InputForm';
import ResultBox from './components/ResultBox';
const apiEndpoints = {
  'sim-swap': 'http://localhost:8000/sim-swap/check',
  'device': 'http://localhost:8000/device-swap/check',
  'call-forwarding': 'http://localhost:8000/call-forwarding',
  'device-retrieval-date': 'http://localhost:8000/device-swap/retrieve-date',
  'sim-retrieval-date': 'http://localhost:8000/sim-swap/retrieve-date',
};

export default function App() {
  const [loadingFor, setLoadingFor] = useState(null);
  const [results, setResults] = useState({});
  const [errors, setErrors] = useState({});

  const makeApiCall = async (type, phoneNumber) => {
    setLoadingFor(type);
    setErrors((prev) => ({ ...prev, [type]: null }));
    setResults((prev) => ({ ...prev, [type]: null }));

    try {
      const res = await fetch(apiEndpoints[type], {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ phoneNumber }),
      });
      if (!res.ok) throw new Error(`Error ${res.status}`);
      const data = await res.json();

      const updatedResults = { [type]: data };

      // Additional calls if sim-swap or device swap detected
      if (type === 'device' && data.swapped === true) {
        try {
          const dateRes = await fetch(apiEndpoints['device-retrieval-date'], {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phoneNumber }),
          });
          if (!dateRes.ok) throw new Error(`Error ${dateRes.status}`);
          const dateData = await dateRes.json();
          updatedResults['device-retrieval-date'] = dateData;
        } catch (e) {
          setErrors((prev) => ({ ...prev, ['device-retrieval-date']: e.message }));
        }
      }

      if (type === 'sim-swap' && data.swapped === true) {
        try {
          const dateRes = await fetch(apiEndpoints['sim-retrieval-date'], {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phoneNumber }),
          });
          if (!dateRes.ok) throw new Error(`Error ${dateRes.status}`);
          const dateData = await dateRes.json();
          updatedResults['sim-retrieval-date'] = dateData;
        } catch (e) {
          setErrors((prev) => ({ ...prev, ['sim-retrieval-date']: e.message }));
        }
      }

      setResults((prev) => ({ ...prev, ...updatedResults }));
    } catch (err) {
      setErrors((prev) => ({ ...prev, [type]: err.message }));
    } finally {
      setLoadingFor(null);
    }
  };

  return (
    <div className="container" style={{ padding: '2rem' }}>
      <h2>Validate Customer</h2>
      <InputForm onCheck={makeApiCall} />

      {Object.keys(apiEndpoints).map((key) => {
        // only display results for main endpoints, not the retrieval-date ones
        if (key === 'device-retrieval-date' || key === 'sim-retrieval-date') return null;
        return (
          <div key={key} style={{ marginTop: '1.5rem' }}>
            {loadingFor === key ? (
              <div className="loading">Loading {key} check...</div>
            ) : (
              <>
                <ResultBox title={key.replace(/-/g, ' ').toUpperCase()} data={results[key]} error={errors[key]} />
                {key === 'device' && results['device-retrieval-date'] && (
                  <ResultBox
                    title="DEVICE SWAP DATE"
                    data={results['device-retrieval-date']}
                    error={errors['device-retrieval-date']}
                  />
                )}
                {key === 'sim-swap' && results['sim-retrieval-date'] && (
                  <ResultBox
                    title="SIM SWAP DATE"
                    data={results['sim-retrieval-date']}
                    error={errors['sim-retrieval-date']}
                  />
                )}
              </>
            )}
          </div>
        );
      })}
    </div>
  );
}
