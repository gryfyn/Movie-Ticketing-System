import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://zoxirczmacculzlpfprg.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpveGlyY3ptYWNjdWx6bHBmcHJnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTg3MDcwMDUsImV4cCI6MjAzNDI4MzAwNX0.KEEyIN11s4L-XgetG8GctUDaHv0oiPMMbaWs91BA7jU';
const supabase = createClient(supabaseUrl, supabaseKey);

export default supabase;
