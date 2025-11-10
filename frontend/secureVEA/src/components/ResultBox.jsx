export default function ResultBox({ title, data, error }) {
  if (!data && !error) return null;

  let msg = '';

  if (error) {
    msg = `Error: ${error}`;
  } else if (data) {
    if (title.toLowerCase().includes('device') && !title.toLowerCase().includes('date')) {
      // device swap check
      if (data.swapped === false) {
        msg = 'No device swap detected';
      } else if (data.swapped === true) {
        msg = 'Device swap detected';
      } else {
        msg = 'No device swap data available or Unknown';
      }
    } else if (title.toLowerCase().includes('sim') && !title.toLowerCase().includes('date')) {
      // sim swap check
      if (data.swapped === false) {
        msg = 'No SIM swap detected';
      } else if (data.swapped === true) {
        msg = 'SIM swap detected';
      } else {
        msg = 'No SIM swap data available or Unknown';
      }
    } else if (title.toLowerCase().includes('call forwarding')) {
      if (data.active === false) {
        msg = 'No call forwarding setup';
      } else if (data.active === true) {
        msg = 'Call forwarding active';
      } else {
        msg = 'No call forwarding data available or Unknown';
      }
    }
    // New case: handle sim/device swap date messages
    else if (title.toLowerCase().includes('sim swap date')) {
      if (data.latestSimChange) {
        msg = `Latest SIM change detected on ${new Date(data.latestSimChange).toLocaleString()}`;
      } else {
        msg = 'No SIM swap date available';
      }
    } else if (title.toLowerCase().includes('device swap date')) {
      if (data.latestDeviceChange) {
        msg = `Latest device change detected on ${new Date(data.latestDeviceChange).toLocaleString()}`;
      } else {
        msg = 'No device swap date available';
      }
    } else {
      msg = 'No relevant data available';
    }
  }

  function prettyPrintObject(obj) {
  if (!obj || Object.keys(obj).length === 0) return null;
  return Object.entries(obj)
    .map(([k, v]) => `  "${k}": ${typeof v === "string" ? `"${v}"` : v}`)
    .join('\n');
}


  return (
    <div>
      <div className="result-box-title">{title}</div>
      <div>{msg}</div>
      {data && Object.keys(data).length > 0 && (
        <pre className="result-box-json">
          {prettyPrintObject(data)}
        </pre>
      )}
    </div>
  );
}