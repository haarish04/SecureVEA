function FormatKey(key) {
  return key
    .replace(/[_-]/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase());
}

// Helper: Generate display message based on key and data
function getResultMessage(title, data, error) {
  if (error) return `Error: ${error}`;

  const t = title.toLowerCase();

  // Device/Sim swap
  if (t.includes('swap') && !t.includes('date')) {
    if (data.swapped === false) return `No ${t.includes('sim') ? "SIM" : "device"} swap detected`;
    if (data.swapped === true) return `${t.includes('sim') ? "SIM" : "Device"} swap detected`;
    return `No ${t.includes('sim') ? "SIM" : "device"} swap data available or Unknown`;
  }
  // Swap date
  if (t.includes('sim swap date') && data.latestSimChange)
    return `Latest SIM change detected on ${new Date(data.latestSimChange).toLocaleString()}`;
  if (t.includes('device swap date') && data.latestDeviceChange)
    return `Latest device change detected on ${new Date(data.latestDeviceChange).toLocaleString()}`;

  // Call forwarding
  if (t.includes('call forwarding')) {
    if (data.active === false) return 'No call forwarding setup';
    if (data.active === true) return 'Call forwarding active';
    return 'No call forwarding data available or Unknown';
  }

  // Location retrieval
  if (t.includes('location') && data.lastLocationTime) {
    return `Latest location as of ${new Date(data.lastLocationTime).toLocaleString()}`;
  }

  // Fallback
  return 'No relevant data available';
}

// Modular recursive pretty printer for nested objects & arrays
function prettyPrintObject(obj, indent = 2) {
  if (!obj || typeof obj !== 'object') return String(obj);
  if (Array.isArray(obj)) {
    return obj
      .map(v => prettyPrintObject(v, indent + 2))
      .join('\n');
  }
  return Object.entries(obj)
    .map(([key, value]) => {
      if (typeof value === 'object' && value !== null) {
        return `${' '.repeat(indent)}"${key}": {\n${prettyPrintObject(value, indent + 2)}\n${' '.repeat(indent)}}`;
      } else {
        return `${' '.repeat(indent)}"${key}": ${typeof value === 'string' ? `"${value}"` : value}`;
      }
    })
    .join('\n');
}

export default function ResultBox({ title, data, error }) {
  if (!data && !error) return null;

  const message = getResultMessage(title, data, error);

  return (
    <div>
      <div className="result-box-title">{FormatKey(title)}</div>
      <div>{message}</div>
      {data && Object.keys(data).length > 0 && (
        <pre className="result-box-json">
          {prettyPrintObject(data)}
        </pre>
      )}
    </div>
  );
}
