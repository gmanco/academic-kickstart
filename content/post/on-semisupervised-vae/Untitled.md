

```python
import torch
import torch.nn as nn

class Decoder(nn.Module):
    def __init__(self, latent_size,out_size):
        super(Decoder, self).__init__()

        self.linear_layer = nn.Linear(latent_size, out_size)
        nn.init.xavier_normal_(self.layer.weight)

    def forward(self, z, y):
        input = torch.cat([z,y],-1)
        
        return self.linear_layer(input)
```


```python
class Encoder_z(nn.Module):
    def __init__(self, input_size,num_classes,latent_size):
        super(Decoder, self).__init__()

        self.linear_layer = nn.Linear(input_size + num_classes, 2*latent_size)
        nn.init.xavier_normal_(self.linear_layer.weight)
        
    def _sample_latent(self, mu, log_sigma):
        sigma = torch.exp(log_sigma)
        epsilon = torch.from_numpy(np.random.normal(0, 1, size=sigma.size())
                                   ,requires_grad=False).to(sigma.device)

        return mu + epsilon*sigma
        
    def forward(self, x):
        temp_out = self.linear_layer(x)
    
        mu = temp_out[:, :self.latent_size]
        log_sigma = temp_out[:, self.latent_size:]

        z = _sample_latent(mu, log_sigma)

        return z, mu, log_sigma
    
    
class Classifier(nn.Module):
    def __init__(self, input_size,num_classes):
        super(Decoder, self).__init__()

        self.linear_layer = nn.Linear(input_size, 2*latent_size)
        nn.init.xavier_normal_(self.layer.weight)
        
        self.softmax = nn.Softmax(dim=-1)
        
    def forward(self, x):
        return self_softmax(self-linear(layer(x))
    
```


      File "<ipython-input-6-cc9dce9e7c48>", line 37
        
        ^
    SyntaxError: unexpected EOF while parsing




```python
def unsupervised_loss(x,encoder,decoder,classifier, y_prior=1):
    y_q = classifier(x)
    kld_cat = torch.mean(torch.sum(y_q*(torch.log(y_q) - torch.log(y_prior)),-1),-1)  
    kld_norm = 0
    
    num_classes = y_q.size(-1)
    e = torch.zeros(y_q.size()).to(x.device)
    
    log_prob_e = []
    for j in range(num_classes):
        e[:,j] = 1.
        z, mu_q, logvar_q = encoder(x,e)
        kld_norm += torch.sum(0.5 * (-logvar_q + torch.exp(logvar_q) + mu_q**2 - 1)
        log_prob_e.append(decoder(z))
        e[:,j] = 0.
        
    kld_norm = torch.mean(kld_norm, -1))

    log_prob_e = torch.floatTensor(log_prob_e)
    log_probs = torch.matmul(llk_e,y_q).squeeze()
    
    loss = nn.NLLLoss()
    llk = loss(log_probs,x)
    
    return llk + kld_cat + kld_norm
```


```python
def supervised_loss(x,y,encoder,decoder,classifier):
    y_q = classifier(x)
    
    z, mu_q, logvar_q = encoder(x,y)
    kld_norm = torch.mean(torch.sum(0.5 * (-logvar_q + torch.exp(logvar_q) + mu_q**2 - 1),-1)

    log_probs = decoder(x)
                          
    loss = nn.NLLLoss()
    llk = loss(log_probs,x)
    
    loss = nn.CrossEntropyLoss()
    llk_cat = loss(y_q,y)
                          
    return llk + llk_cat + kld_norm    
```


      File "<ipython-input-2-829e11dca8e4>", line 7
        log_probs = decoder(x)
                ^
    SyntaxError: invalid syntax




```python
class SSVAE(nn.Module):
    def __init__(self,input_size,num_classes,latent_size, y_prior = 1):
        self.input_size = input_size
        self.num_classes = num_classes
        self.latent_size = latent_size
        
        self.y_prior = y_prior
        
        self.encoder = Encoder(input_size,num_classes,latent_size)
        self.decoder = Decoder(latent_size,input_size)
        self.classifier = Classifier(input_size, num_classes)
        
        llk_loss = nn.NLLLoss()
        cat_loss = nn.CrossEntropyLoss()

    def unsupervised_loss(self, x):
        y_q = self.classifier(x)
        kld_cat = torch.mean(torch.sum(y_q*(torch.log(y_q) - torch.log(self.y_prior)),-1),-1)  
        kld_norm = 0
    
        e = torch.zeros(y_q.size()).to(x.device)
    
        log_prob_e = []
        for j in range(self.num_classes):
            e[:,j] = 1.
            z, mu_q, logvar_q = self.encoder(x,e)
            kld_norm += torch.sum(0.5 * (-logvar_q + torch.exp(logvar_q) + mu_q**2 - 1)
            log_prob_e.append(self.decoder(z))
            e[:,j] = 0.
        
        kld_norm = torch.mean(kld_norm, -1))

        log_prob_e = torch.floatTensor(log_prob_e)
        log_probs = torch.matmul(llk_e,y_q).squeeze()
    
        llk = llk_loss(log_probs,x)
    
        return llk + kld_cat + kld_norm
        
        
    def supervised_loss(self,x,y):
        z, mu_q, logvar_q = self.encoder(x,y)
        kld_norm = torch.mean(torch.sum(0.5 * (-logvar_q + torch.exp(logvar_q) + mu_q**2 - 1),-1)

        log_probs = self.decoder(x)                          
        llk = loss(log_probs,x)
    
        y_q = self.classifier(x)
        llk_cat = cat_loss(y_q,y)
                          
        return llk + llk_cat + kld_norm    
        
    def forward(self, x, y = None, train = False)
        if not train:
            return self.classifier(x)
        else:
            if y is not None:
                loss = self.supervised_loss(x,y)
            else
                loss = self.unsupervised_loss(x)
            return loss
```


```python
def train(data_loader,input_size, num_classes, latent_size, y_priors):
    model = SSVAE(input_size,num_classes, latent_size)
    
    optimizer = torch.optim.Adam(model.parameters(), lr = 0.0001)
    
    for batch_idx,(x,y) in enumerate(data_loader):
        optimizer.zero_grad()
        
        loss = model(x,y)
        loss.backward()
        optimizer.step()
```
